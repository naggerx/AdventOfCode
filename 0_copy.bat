@echo off

if [%1]==[] goto usage

copy 0x.py %1.py
copy NUL %1_in.txt
copy NUL %1_in0.txt

"C:\Program Files\Notepad++\notepad++.exe" %1.py %1_in0.txt %1_in.txt 
goto :eof

:usage
echo usage: %0 "<day_number>"
pause
exit /B 1
