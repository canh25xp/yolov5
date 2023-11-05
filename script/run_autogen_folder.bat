@echo off
cd ..

python idcard/idcard.py --source data\images\autogen --name autogen --rotate --save-conf --save-txt --max-det 1 >> runs/autogen.txt

echo Finish !
pause