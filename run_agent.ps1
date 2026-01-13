# AutoStream Agent Runner Script (PowerShell)
# This script activates the venv and runs the agent

Write-Host "Activating virtual environment..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

Write-Host "Running AutoStream Agent..." -ForegroundColor Green
python app\main.py
