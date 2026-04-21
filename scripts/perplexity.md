# Perplexity API Cheat Sheet

## Environment variable

- `PERPLEXITY_API_KEY`

## Endpoint

```
POST https://api.perplexity.ai/chat/completions
```

Headers:
```
Authorization: Bearer $PERPLEXITY_API_KEY
Content-Type: application/json
```

Body (minimum):
```json
{
  "model": "sonar-pro",
  "messages": [
    {"role": "user", "content": "Your research question"}
  ]
}
```

Response: `choices[0].message.content` has the answer. Use `sonar-pro` for research — it includes web citations.

## Example curl

```bash
curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [{"role":"user","content":"What are the top overnight news items moving US stock market futures today?"}]
  }' | jq -r .choices[0].message.content
```

## Good queries for Bull

**Pre-market market context:**
> "What are the top overnight news items moving US stock market futures today [date]? Include S&P 500 futures move, key macro data, and any Fed-related headlines."

**Today's earnings calendar:**
> "Which large-cap US companies are reporting earnings today [date], before open or after close? For each, what is the consensus EPS estimate and any notable guidance risk?"

**Position check:**
> "Has there been any material news, analyst action, or catalyst for ticker [SYMBOL] in the last 24 hours? Include anything about the broader sector."

**Buy candidate discovery:**
> "Name 3–5 large-cap US stocks ($10B+ market cap, liquid, not biotech) that reported positive earnings surprises in the last week with raised guidance AND are trading in a clear uptrend (price above 50-day moving average). For each, list the specific catalyst and why it matters."

**Thesis break check (midday when a position is -7%):**
> "Is there specific news today [date] that explains a drop in [SYMBOL]? Rate the severity: (1) material thesis-breaker, (2) sector-wide noise, (3) unrelated market move."

## Budget tip

Perplexity calls cost money. One Perplexity call per research question, not one per idea. Batch related questions.
