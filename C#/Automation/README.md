# AHS-Automation
Automation project for Advanced Health Services

# Installation
This is a Windows based project. Installation instructions assume that you have access to typical Windows-based tools.

## Clone

Clone this repository to an accessible location.

## WinAppDriver

Install from https://github.com/microsoft/WinAppDriver/releases/download/v1.2.1/WindowsApplicationDriver_1.2.1.msi

## Scoop Local

1. Using Windows Powershell: `iwr -useb get.scoop.sh | iex`
	- If you get an error, run this command in Windows Powershell: `Set-ExecutionPolicy RemoteSigned -scope CurrentUser` then try the previous command again.

## Allure Local

1. Using Windows Powershell: `scoop install allure`
2. Add to path (If not there already:
	- ALLURE_HOME: C:\Users\\<you>\scoop\apps\allure\current
	- ALLURE_CONFIG: <project_directory>\allure\allureConfig.json

If you are unable to access your environment variables, do the following:

1. Using Windows Powershell: $env:ALLURE_CONFIG='<project_directory>\allure\allureConfig.json'
[environment]::setEnvironmentVariable('ALLURE_CONFIG',$env:ALLURE_CONFIG,'User')

## Python

1. Install from https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
2. Add to Path (If not there already): C:\Users\<you>\AppData\Local\Programs\Python\Python37\