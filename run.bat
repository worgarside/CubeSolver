@echo off
IF %1.==. GOTO No1

python PC/%1.py

GOTO End1

:No1
  python PC/main.py
GOTO End1

:End1
