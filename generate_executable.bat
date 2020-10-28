@echo off
title Generating Beth executable

echo Begin

echo Run pyinstaller
@REM venv\Scripts\pyinstaller --onefile main.py --name Beth --log-level=DEBUG --additional-hooks-dir=.
venv\Scripts\pyinstaller --onefile main.py --name Beth --additional-hooks-dir=.
@REM venv\Scripts\pyinstaller main.spec

echo End