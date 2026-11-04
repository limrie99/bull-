#!/usr/bin/env python3
"""Size the SPY index floor. This never places an order and never uses margin.

Bull's Trader voice still sends the order through the existing Alpaca path in
scripts/alpaca.md: a plain market order, time_in_force day, whole shares.
A buy of the floor does not get a stop. A top-up does not count as one of the
three stock buys for the week.

The target is residual, not a fixed percent: SPY owns every dollar that is
not the cash cushion and not already in a conviction stock. On the 2026-11-04
book that is about half the account, because four stocks plus a $10,000
cushion leave the rest for the index.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


# The standing cushion is about $10,000. The older 10% floor still applies:
# never leave less than $10,000, and never leave less than 10% of equity.
CASH_BUFFER_DOLLARS = 10_000.0
CASH_BUFFER_FRACTION = 0.10
INDEX_SYMBOL = "SPY"

# Same submission shape as scripts/alpaca.md. No stop on the index sleeve.
MARKET_ORDER = {"type": "market", "time_in_force": "day", "stop": None}


def cash_buffer(equity: float) -> float:
    """Dollars that must stay in cash. Larger of $10,000 and 10% of equity."""
    equity = float(equity)
    if equity < 0:
        raise ValueError("equity cannot be negative")
    return max(CASH_BUFFER_DOLLARS, CASH_BUFFER_FRACTION * equity)


def stock_market_value(positions: list[dict]) -> float:
    """Market value of conviction stocks. SPY is the floor, not a stock slot."""
    total = 0.0
    for position in positions:
        symbol = str(position.get("symbol", "")).upper()
        if symbol == INDEX_SYMBOL:
            continue
        total += float(position["qty"]) * float(position["price"])
    return total


def spy_shares(positions: list[dict]) -> float:
    for position in positions:
        if str(position.get("symbol", "")).upper() == INDEX_SYMBOL:
            return float(position["qty"])
    return 0.0


def spy_target(equity: float, stock_value: float, buffer: float | None = None) -> dict:
    """SPY should hold everything that is not a stock slot and not the cushion."""
    equity = float(equity)
    stock_value = float(stock_value)
    buffer = cash_buffer(equity) if buffer is None else float(buffer)
    dollars = equity - buffer - stock_value
    pct = (dollars / equity * 100.0) if equity else 0.0
    return {
        "spy_target_dollars": round(dollars, 2),
        "spy_target_pct": round(pct, 2),
        "buffer": round(buffer, 2),
    }


def _none(reason: str, *, equity: float, cash: float, buffer: float, target: dict, extra: dict | None = None) -> dict:
    plan = {
        "action": "none",
        "symbol": INDEX_SYMBOL,
        "qty": 0,
        "estimated_dollars": 0.0,
        "cash_before": round(float(cash), 2),
        "cash_after": round(float(cash), 2),
        "buffer": round(float(buffer), 2),
        "counts_against_weekly_buy_cap": False,
        "order": None,
        "reason": reason,
        **target,
    }
    if extra:
        plan.update(extra)
    return plan


def plan_spy_floor(
    *,
    equity: float,
    cash: float,
    spy_price: float,
    spy_shares_held: float,
    stock_market_value: float,
    qualifying_stock_buy_dollars: float = 0.0,
    daily_loss_cap_hit: bool = False,
    mode: str = "paper",
) -> dict:
    """Decide whether to buy SPY, trim SPY to fund a stock, or do nothing.

    Share counts are rounded so cash cannot fall through the cushion.
    Buying power is intentionally not an input: paper buying power is margin,
    and this book does not use margin.
    """
    equity = float(equity)
    cash = float(cash)
    price = float(spy_price)
    held = float(spy_shares_held)
    stock_value = float(stock_market_value)
    stock_buy = float(qualifying_stock_buy_dollars)
    if price <= 0:
        raise ValueError("spy_price must be positive")
    if cash < 0 or stock_buy < 0 or held < 0:
        raise ValueError("cash, shares, and stock-buy dollars cannot be negative")

    buffer = cash_buffer(equity)
    target = spy_target(equity, stock_value, buffer)
    target["spy_shares_held"] = held
    target["spy_price"] = round(price, 4)
    target["mode"] = mode

    if str(mode).lower() != "paper":
        return _none(
            "Paper trading only. This calculator will not size a live order.",
            equity=equity, cash=cash, buffer=buffer, target=target,
        )
    if daily_loss_cap_hit:
        return _none(
            "The book is down more than 3% today, so no new buys, including the index floor.",
            equity=equity, cash=cash, buffer=buffer, target=target,
        )

    # A stock that cleared the gate is funded first. If paying for it would
    # break the cushion, sell the fewest SPY shares that refill the cushion.
    # If the stock buy fits, do not also sweep cash in this same run.
    if stock_buy > 0:
        shortfall = stock_buy + buffer - cash
        if shortfall <= 0:
            return _none(
                "A qualifying stock buy is being placed this run, and cash still covers it plus the cushion. Do not also buy SPY in this same run. The next run sweeps whatever cash is still idle.",
                equity=equity, cash=cash, buffer=buffer, target=target,
            )
        qty = int(math.ceil(shortfall / price))
        qty = min(qty, int(held))
        if qty < 1:
            return _none(
                "The stock buy needs more cash than the cushion allows, and there is no SPY share to sell. Skip the stock buy rather than dropping cash under the cushion or using margin.",
                equity=equity, cash=cash, buffer=buffer, target=target,
            )
        proceeds = qty * price
        return {
            "action": "trim",
            "symbol": INDEX_SYMBOL,
            "qty": qty,
            "estimated_dollars": round(proceeds, 2),
            "cash_before": round(cash, 2),
            "cash_after": round(cash + proceeds - stock_buy, 2),
            "buffer": round(buffer, 2),
            "counts_against_weekly_buy_cap": False,
            "order": {**MARKET_ORDER, "side": "sell"},
            "reason": (
                "Trim the index floor so the stock buy can pay for itself and cash stays at the cushion. "
                "This sell is not one of the three weekly stock buys. Do not put a stop on the SPY that remains."
            ),
            **target,
        }

    excess = cash - buffer
    # Also don't buy past the residual target. On a normal day these match,
    # because cash above the cushion is exactly the hole in the SPY sleeve.
    room = target["spy_target_dollars"] - (held * price)
    deploy = min(excess, max(room, 0.0))
    qty = int(deploy // price)
    while qty > 0 and (cash - qty * price) + 1e-6 < buffer:
        qty -= 1
    if qty < 1:
        return _none(
            "Cash is already within one SPY share of the cushion. Nothing to sweep.",
            equity=equity, cash=cash, buffer=buffer, target=target,
        )
    dollars = qty * price
    cash_after = cash - dollars
    return {
        "action": "buy",
        "symbol": INDEX_SYMBOL,
        "qty": qty,
        "estimated_dollars": round(dollars, 2),
        "cash_before": round(cash, 2),
        "cash_after": round(cash_after, 2),
        "buffer": round(buffer, 2),
        "counts_against_weekly_buy_cap": False,
        "order": {**MARKET_ORDER, "side": "buy"},
        "reason": (
            f"No stock buy this run, and cash is above the ${buffer:,.0f} cushion. "
            f"Buy {qty} shares of SPY, about ${dollars:,.0f}, so the idle dollars track the market today. "
            "This does not use one of the three weekly stock buys, does not take a stock slot, "
            "and does not get a stop. Leave the cushion in cash. Do not use buying power."
        ),
        **target,
    }


def plan_from_snapshot(snapshot: dict) -> dict:
    positions = list(snapshot.get("positions") or [])
    if "stock_market_value" in snapshot:
        stocks = float(snapshot["stock_market_value"])
    else:
        stocks = stock_market_value(positions)
    shares = snapshot.get("spy_shares")
    if shares is None:
        shares = spy_shares(positions)
    return plan_spy_floor(
        equity=float(snapshot["equity"]),
        cash=float(snapshot["cash"]),
        spy_price=float(snapshot["spy_price"]),
        spy_shares_held=float(shares),
        stock_market_value=stocks,
        qualifying_stock_buy_dollars=float(snapshot.get("qualifying_stock_buy_dollars") or 0),
        daily_loss_cap_hit=bool(snapshot.get("daily_loss_cap_hit") or False),
        mode=str(snapshot.get("mode") or "paper"),
    )


def _load_snapshot(args: argparse.Namespace) -> dict:
    if args.fixture:
        return json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    required = ("equity", "cash", "spy_price")
    missing = [name for name in required if getattr(args, name) is None]
    if missing:
        raise SystemExit(f"Need --fixture or {', '.join('--' + m.replace('_', '-') for m in missing)}")
    snapshot = {
        "equity": args.equity,
        "cash": args.cash,
        "spy_price": args.spy_price,
        "spy_shares": args.spy_shares if args.spy_shares is not None else 0,
        "qualifying_stock_buy_dollars": args.stock_buy_dollars or 0,
        "daily_loss_cap_hit": bool(args.daily_loss_cap),
        "mode": args.mode,
    }
    if args.stock_market_value is not None:
        snapshot["stock_market_value"] = args.stock_market_value
    else:
        snapshot["positions"] = []
        snapshot["stock_market_value"] = 0
    return snapshot


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dry-run the SPY cash sweep. Does not place an order.")
    parser.add_argument("--fixture", help="JSON snapshot, including today's book")
    parser.add_argument("--equity", type=float)
    parser.add_argument("--cash", type=float)
    parser.add_argument("--spy-price", type=float)
    parser.add_argument("--spy-shares", type=float)
    parser.add_argument("--stock-market-value", type=float)
    parser.add_argument("--stock-buy-dollars", type=float, default=0.0)
    parser.add_argument("--daily-loss-cap", action="store_true")
    parser.add_argument("--mode", default="paper")
    args = parser.parse_args(argv)
    plan = plan_from_snapshot(_load_snapshot(args))
    json.dump(plan, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
