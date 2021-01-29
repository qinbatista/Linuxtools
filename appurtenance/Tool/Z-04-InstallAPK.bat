@echo off
set "str=%~nx1"
adb install -r %str%
