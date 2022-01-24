@echo off

rd /s /q allure-report
rd /s /q allure-results

start cmd /k "call wad-start.bat"

dotnet test

call allure-generate.bat

pause