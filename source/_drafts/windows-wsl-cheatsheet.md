---
title: Qt开发经验
date: 2023-01-16 10:00:00
update: 2023-01-16 10:00:00

categories:
 - windows开发
 
tags: 
 - windows
 - WSL
 - cheatsheet
 
keywords:
 - WSL
 - cheatsheet
---

# Windows下WSL的使用

*注意：* WSL版本为： 2

```
C:\Windows\System32>wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-22.04    Stopped         2

C:\Windows\System32>wsl --export Ubuntu-22.04 L:\ubuntu22.04_wsl.tar

C:\Windows\System32>wsl --unregister Ubuntu-22.04
Unregistering...

C:\Windows\System32>wsl --import Ubuntu-22.04 E:\WSL\Ubuntu2204 L:\ubuntu22.04_wsl.tar

C:\Windows\System32>wsl -l
Windows Subsystem for Linux Distributions:
Ubuntu-22.04 (Default)

C:\Windows\System32>ubuntu2204.exe

root@DESKTOP-SQB192A:~/socket# exit

C:\Windows\System32>wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-22.04    Running         2

C:\Windows\System32>wsl --shutdown

C:\Windows\System32>wsl -l
Windows Subsystem for Linux Distributions:
Ubuntu-22.04 (Default)

C:\Windows\System32>wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-22.04    Stopped         2
```
