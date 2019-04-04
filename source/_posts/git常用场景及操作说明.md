---
title: git基本操作说明及常用场景
date: 2017-04-23 08:16:17
update: 2017-04-23 22:03:23

categories:
- Linux技术
 
tags: 
- 开发工具

keywords:
 - git基本操作
 - git分支场景
 - 版本控制神器
---

## 前言

该文章记录了git的基本使用命令和一些实例，
包含初始化一个仓库（repository）、开始或停止跟踪（track）文件、暂存（stage）或提交（commit)更改，
向远程仓库推送（push）以及拉取（pull）文件。

## 基本操作

```bash git基本使用
# myprojecty工程版本控制
mkdir myproject;cd myproject
# 创建版本库 git init
git init

# 设置当前git用户信息
git config --local user.name lxyboy
git config --local user.email lxyboy@hotmail.com

# git add 添加文件到暂存区
git add filename
# git commit 对暂存区的文件生成快照
git commit filename

# 查看状态
git status
# 查看区别
git diff 

#  清空所有未暂存更改(注意有个点)
git checkout .
#   清空未暂存更改(文件)  这个命令很危险，因为会清除工作区中未提交的改动，代码丢失
git checkout -- filename

# 清除未暂存的
git clean -nfd 预览
git clean -fd 删除

# 远端操作 集中式工作流
# git pull = git fetch +  git merge
git pull origin master
git push origin master
# 更多实例
git remote add oschina https://****
git push oschina restful:master
git push origin <local_branch_name>:<remote_branch_name>
git push origin zhoujiadu:zhoujiadu

# 列出远程仓库信息
git remote -v
git remote show origin

# 新建分支并切换到分支工作
git checkout -b newbranch
# 列出所有分支
git branch -a
# 列出远程分支
git branch --remotes
# 删除远程分支
git branch --remotes -d oschina/master 

# git 打包 tar.gz
git archive --format=tar --prefix=name-0.1/ branch_name | gzip > name-0.1.tar.gz

# git统计作者代码行数
git log --author="luxy" --pretty=tformat: --numstat | gawk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "Added lines: %s! Removed lines : %s Total lines: %s\n",add,subs,loc }'
```

## git中忽略文件

一般我们总会有些文件无需纳入 Git 的管理，
也不希望它们总出现在未跟踪文件列表。 
通常都是些自动生成的文件，比如日志文件，或者编译过程中创建的临时文件等。 
在这种情况下，我们可以创建一个名为 `.gitignore` 的文件，列出要忽略的文件模式。

```txt .gitignore例子
# 忽略所有build目录
build/
```

一些有用的.gitignore模板: [https://github.com/github/gitignore](https://github.com/github/gitignore)

## git使用代理

http(s) 协议配置代理vim ~/.gitconfig

```txt
[http]
proxy = socks5://127.0.0.1:6600
```

## 保存密码

`git config --local credential.helper store`
输入用户密码后会把密码保存在`~/.git=credentials`文件里。

相当于进行如下操作编辑`vim ~/.git-credentials`:

```txt .git-credentials
http(s)://{username}:{password}@{domain}
```

取消的方法为删除git库中`.git/config` 中的`credential`节的内容

## 其他注意事项
自己部署gitlab反向代理使用nginx时注意nginx配置中添加`client_max_body_size 50m;`
否则git文件过大可能无法提交

## Git: error: RPC failed; result=22, HTTP code = 411

上传文件大导致错误

```bash
git config http.postBuffer 524288000
```