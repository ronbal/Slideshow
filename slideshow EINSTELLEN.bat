
@echo off
SET count=10
SET subnet=10.110.20

:start
SET /a count=%count%+1

ECHO ...scanning...
ping -a -n 1 -w 500 %subnet%.%count% | FIND "SLIDESHOW"
IF %errorlevel%==0 (start /d "" IEXPLORE.EXE %subnet%.%count%
					goto :eof)


GOTO start