@echo off
setlocal

cd /d "%~dp0"

if not exist "%~dp0index.html" (
  echo index.html not found in this folder.
  pause
  exit /b 1
)

set "TARGET=%~dp0index.html"
set "EDGE_EXE=C:\Program Files\Microsoft\Edge\Application\msedge.exe"
set "CHROME_EXE=C:\Program Files\Google\Chrome\Application\chrome.exe"
set "CHROME_EXE_X86=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
set "CHROME_EXE_USER=%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"

echo Opening TextureCreate...

if exist "%EDGE_EXE%" (
  start "" "%EDGE_EXE%" "%TARGET%"
  exit /b 0
)

if exist "%CHROME_EXE%" (
  start "" "%CHROME_EXE%" "%TARGET%"
  exit /b 0
)

if exist "%CHROME_EXE_X86%" (
  start "" "%CHROME_EXE_X86%" "%TARGET%"
  exit /b 0
)

if exist "%CHROME_EXE_USER%" (
  start "" "%CHROME_EXE_USER%" "%TARGET%"
  exit /b 0
)

echo Edge/Chrome not found. Opening with default browser...
start "" "%TARGET%"

exit /b 0
