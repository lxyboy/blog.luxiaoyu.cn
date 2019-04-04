title: Hexo转移
author: admin
tags:
  - Hexo
  - 博客
categories:
  - linux技术
date: 2019-04-03 19:00:00
---
记录hexo转移

#### 使用git管理hexo blog

需要track的文件清单

|文件名|作用|注意事项|
|----|----|---|
|_admin-config.yml|供Hexo-admin使用|无|
|_config.yml|供Hexo使用|注意其中的私密信息（密码，token等信息）不能上传git|
|package.json|用户搭建hexo及项目|无|
|db.json|Hexo数据库|无|
|source|文章及其他page的源文件|需要git控制|
|source/uploads|上传的图片或者文件|需要git控制|
