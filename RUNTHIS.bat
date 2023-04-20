@echo off
set fullscreen=%temp%\tempkeys.vbs
if exist "%fullscreen%" del /f /q "%fullscreen%"
echo set wshshell = wscript.createobject("wscript.shell")>>"%fullscreen%"
echo wshshell.sendkeys"{F11}">>"%fullscreen%"
cscript //nologo "%fullscreen%"
cmd /k "python astro.py"