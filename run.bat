@echo off

IF [%1] == [] GOTO No1

IF "%1" == "test" GOTO No2

python Codebase/main.py %1

GOTO End1

:No1
  python Codebase/main.py
GOTO End1

:No2
  python Codebase/test.py
GOTO End1

:End1
