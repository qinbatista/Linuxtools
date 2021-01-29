
@echo off
set "str=%~nx1"
set "str1=%~dp1%~nx1"


call dex2jar\dex2jar.bat %str%

DEL  %str%


@echo %str%

