@echo off
call env.bat

python idcard/idcard.py --source data\images\autogen_small --name autogen_small --rotate --save-conf --save-txt --max-det 1

echo Finish !
pause