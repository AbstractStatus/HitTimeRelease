@echo off
rem Double-click launcher for gen_index.py (Windows)
rem Switches console to UTF-8 so Python's Chinese output renders correctly.
chcp 65001 >nul
set PYTHONIOENCODING=utf-8

rem Always run from the directory where this .bat lives.
cd /d "%~dp0"

rem Pick a real Python interpreter: prefer the "py" launcher, then "python".
set "PY_CMD="
py -3 -c "import sys" >nul 2>&1 && set "PY_CMD=py -3"
if not defined PY_CMD (
    python -c "import sys" >nul 2>&1 && set "PY_CMD=python"
)

if not defined PY_CMD (
    echo [ERROR] Python 3 was not found. Please install Python 3 first:
    echo         https://www.python.org/downloads/
    pause
    exit /b 1
)

%PY_CMD% gen_index.py

if errorlevel 1 (
    echo.
    echo [ERROR] gen_index.py failed. Check the message above.
)

pause
