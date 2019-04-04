---
title: Hexo安装部署
date: 2017-04-05 08:16:17

categories:
- Linux技术
 
tags: 
- blog
- linux日常

keywords:
 - hexo
 - hexo安装
 - hexo安装配置
 - hexo部署
 - 独立博客

---

## 前言

以前的独立Blog是自己通过Django写的托管在了sinaapp上，
又是一个新的开始，开启我的Hexo之旅，很高心她能成为我的记忆簿，记录我的学习生活~


## 安装

hexo是基于nodejs开发的安装起来非常容易，参照hexo官网即可安装成功
下面说一下需要注意的事项和相关插件

1. [hexo-generator-feed](https://github.com/hexojs/hexo-generator-feed)
    用来生成RSS的工具

2. [hexo-algoliasearch](https://github.com/LouisBarranqueiro/hexo-algoliasearch) 与 [hexo-algolia](https://github.com/oncletom/hexo-algolia)
    这两个工具都是通过algoli[^1]这个网站用来提供搜索功能的
    在配置这个的过程中有个坑，希望大家注意 algolia 在站点下的配置文件`_config.yml`:
    ```yml
    algolia:
      appId: 'yourappkey'
      apiKey: 'yourapikey'
      adminApiKey: 'youradminkey'
      indexName: 'yourindexname'
      chunkSize: 5000
      fields:
        - title
        - slug
        - path
        - content:strip
    ```
    fields中的`path`很重要，页面就是根据这个跳转的
    
3. [hexo-theme-next](https://github.com/iissnan/hexo-theme-next) 
    本博客使用的主题，我觉得该主题做的不错，已经满足我的需求了。
    在配置主题的时候我建议参考 https://github.com/iissnan/hexo-theme-next/wiki 里面有详细的描述。
    感谢该主题的作者
    
4. 关于markdown高级语法 [hexo-renderer-markdown-it](https://github.com/celsomiranda/hexo-renderer-markdown-it)
    刚开始装好后我想要使用脚注就用了`[^1]`标签，但是无效:cry:, 查找资料发现如果要使用类似footnote，emoji等高级markdown拓展语法
    需要安装额外的插件具体的安装方法上面的软件描述的很清楚，我这里总结一下关系`hexo-renderer-markdown-it` -> `markdown-it` -> `各个markdown-it插件`


## 远程主机部署hexo-deployer-sftp

直接通过sftp进行上传
配置方法[传送门](https://hexo.io/docs/deployment.html#SFTP)

  
## 使用基本命令

```bash
hexo n pageName #创建一个名为pageName的页面
hexo g #生成页面文件
hexo s #在本地查看页面效果
hexo d #将生成的页面文件部署到远程服务器中
```

## 注意

* hexo s 页面会进行数据缓存，导致在配置后之前页面的缓存没修改，看不到修改状态。使用http-server代替。

[^1]: [www.algolia.com](https://www.algolia.com/) : 感觉这个网站做的不错啊，网速快，功能简单，关键免费。
