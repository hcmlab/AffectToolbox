@echo off
cd /d "%~dp0"
uv run --locked --managed-python main.py
pause
