@echo off
IF %1.==. GOTO No1

python Codebase/%1.py

GOTO End1

:No1
  python Codebase/main.py
GOTO End1

:End1
