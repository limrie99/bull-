@echo off
REM Bull dashboard launcher
REM - Runs a `git pull` loop in the background to sync cloud-routine updates
REM - Serves the project folder on http://localhost:8008
REM - Opens the dashboard in your browser
REM Close this window to stop everything.

cd /d "%~dp0"

REM Background: pull from origin/main every 30 seconds so local dashboard sees cloud updates
start "bull-git-pull" /min cmd /c "for /l %%i in (1,0,2) do (git pull --quiet origin main 2>nul & timeout /t 30 /nobreak >nul)"

REM Open dashboard in default browser
start "" http://localhost:8008/dashboard/

REM Foreground: serve the project folder
python -m http.server 8008
