@echo off
cd ..

set CWD=.

set RELEASE=D:\Projects\C_Cpp\Yolov5-segmentation-ncnn\x64\Release
set OUTPUT_FOLDER=%CWD%\runs\idcard\autogen
set LOG_PATH=%CWD%\runs\compareAngles-autogen.txt

if exist %LOG_PATH% del %LOG_PATH%

echo Running...

%RELEASE%\compareAngles.exe %OUTPUT_FOLDER%\rotate\angle.txt >> %LOG_PATH%

echo Finish !
pause