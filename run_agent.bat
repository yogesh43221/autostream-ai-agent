@echo off
REM AutoStream Agent Runner Script
REM This script activates the venv and runs the agent

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Running AutoStream Agent...
python app\main.py

pause
