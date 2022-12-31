@echo off
cd /d %~dp0
call activate torch

python run_ui.py

pause 