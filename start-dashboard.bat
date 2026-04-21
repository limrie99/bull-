@echo off
REM Bull dashboard launcher
REM Serves the project folder on http://localhost:8008 and opens the dashboard.
REM Close this window to stop the server.

cd /d "%~dp0"
start "" http://localhost:8008/dashboard/
python -m http.server 8008
