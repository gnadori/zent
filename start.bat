@echo off
title Zent Presenter & Pacer
echo Inditas...
python server.py
if %ERRORLEVEL% NEQ 0 (
    echo Python nem talalhato, inditas kozvetlen bongeszoben...
    start index.html
)
pause
