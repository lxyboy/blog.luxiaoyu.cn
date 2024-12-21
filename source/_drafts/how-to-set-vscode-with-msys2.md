title: 如何设置msys2为默认的vscode integration terminal
author: admin
tags:
  - Hexo
  - 博客
categories:
  - vscode
  - linux技术
date: 2024-12-03 19:00:00
---
## 记录如何使用msys2作为vscode的默认integration terminal

### 配置settings.json

打开settings.json

```
# 快捷键 Ctrl + Shift + P
# Open User Settings (JSON)
```

编辑

`C:\\Local\\msys64\\msys2_shell.cmd` 这个是你msys2的安装路径

```
    "terminal.integrated.defaultProfile.windows": "MSYS2",
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "icon": "terminal-powershell"
        },
        "Command Prompt": {
            "path": [
                "${env:windir}\\Sysnative\\cmd.exe",
                "${env:windir}\\System32\\cmd.exe"
            ],
            "args": [],
            "icon": "terminal-cmd"
        },
        "MSYS2": {
            "path": "C:\\Local\\msys64\\msys2_shell.cmd",
            "args": [
                "-defterm",
                "-here",
                "-no-start",
            ]
        }
    }
```
