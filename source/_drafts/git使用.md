#Git 使用

##基本
git config --global user.name lxyboy
git config --global user.email lxyboy@hotmail.com

##git会记录所有commit所以在commit的时候确保该commit是有意义的

## git使用代理

http(s) 协议配置代理vim ~/.gitconfig

```txt
[http]
proxy = socks5://127.0.0.1:6600
```

## 常用

#### 列出远程仓库

git remote -v

#### 列出远程仓库信息

git remote show origin

#### 分支

```bash
# 列出所有分支
git branch -a
# 列出远程分支
git branch --remotes
# 删除远程分支
git branch --remotes -d oschina/master 
```

#### 清空未暂存更改
git checkout . (注意有个点) 或 git checkout -- filename
使用暂存区的全部文件 或 指定文件 替换工作区的文件
-- 这个命令很危险，因为会清除工作区中未提交的改动

清楚未暂存的
git clean -nfd 预览
git clean -fd 删除

#### 提交本地分支restful到远程分支master


```bash
git remote add oschina https://****
git push oschina restful:master

git push origin <local_branch_name>:<remote_branch_name>

git push origin zhoujiadu:zhoujiadu
```

#### 切到远程的某分支下,远程分支是无法编辑的必须创建新分支

git checkout -t remotes/origin/stable/juno
**或**
git checkout -b stable/juno remotes/origin/stable/juno

#### 新建分支并切换到分支工作
git checkout -b newbranch

#### git 打包 tar.gz

git archive --format=tar --prefix=vdistack-0.1/ branch_name | gzip > vdistack-0.1.tar.gz

## 统计

#### 统计作者行数
git log --author="lxyboy" --pretty=tformat: --numstat | gawk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "Added lines: %s! Removed lines : %s Total lines: %s\n",add,subs,loc }'


## 保存密码
vim /home/chinaestone/.git-credentials
https://{username}:{password}@github.com
git config --global credential.helper store

## 自己部署gitlab反向代理使用nginx时注意
否则过大可能无法提交
client_max_body_size 50m;