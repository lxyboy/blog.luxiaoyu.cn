# 树莓派RPi与Redmine

## 在树莓派上安装 Redmine

### 参考Redmine安装wiki

参考[https://www.redmine.org/projects/redmine/wiki/RedmineInstall](https://www.redmine.org/projects/redmine/wiki/RedmineInstall)说明

#### 安装Ruby

```
apt search ruby
apt install ruby ruby-dev sqlite3 libyaml-dev
# optional
apt install imagemagick ghostscript
```

```
# 使用下面找到ruby版本
root@py4:~# apt search ruby
ruby/stable 1:3.1 arm64
  Interpreter of object-oriented scripting language Ruby (default version)
# 安装 ruby
root@py4:~# apt install ruby ruby-dev
The following additional packages will be installed:
  fonts-lato javascript-common libjs-jquery libruby libruby3.1 rake ruby-net-telnet ruby-rubygems ruby-sdbm
  ruby-webrick ruby-xmlrpc ruby3.1 rubygems-integration
Suggested packages:
  ri ruby-dev bundler
The following NEW packages will be installed:
  fonts-lato javascript-common libjs-jquery libruby libruby3.1 rake ruby ruby-net-telnet ruby-rubygems
  ruby-sdbm ruby-webrick ruby-xmlrpc ruby3.1 rubygems-integration
root@py4:~# ruby --version
ruby 3.1.2p20 (2022-04-12 revision 4491bb740a) [aarch64-linux-gnu]
```

观察安装得知Ruby是3.1

#### 安装Rails 

对于gem的安装需要重新设定gem的源， 国外的源无法接通, 参照[https://mirrors.ustc.edu.cn/help/rubygems.html](https://mirrors.ustc.edu.cn/help/rubygems.html)。

```
gem sources # 列出默认源
gem sources --remove https://rubygems.org/ # 移除默认源
gem sources -a https://mirrors.ustc.edu.cn/rubygems/ # 添加科大源
# 安装 rails
gem install rails -V
```

```
root@py4:~# gem sources # 列出默认源
root@py4:~# gem sources --remove https://rubygems.org/ # 移除默认源
root@py4:~# gem sources -a https://mirrors.ustc.edu.cn/rubygems/ # 添加科大源
https://mirrors.ustc.edu.cn/rubygems/ added to sources

root@py4:~# gem install rails sidekiq

root@py4:~# rails --version
Rails 7.2.2.1
```
#### 下载Redmine并安装

根据版本信息

* Rails 7.2.2.1
* ruby 3.1.2p20

选择```redmine-6.0.2.tar.gz```

```
wget https://www.redmine.org/releases/redmine-6.0.2.tar.gz
tar xf redmine-6.0.2.tar.gz;cd redmine-6.0.2
```

#### 配置数据库

```
cp config/database.yml.example config/database.yml
```

```
production:
  adapter: sqlite3
  database: db/redmine.sqlite3
```

#### 安装redmine依赖

```
gem install bundler
bundle config set --local without 'development test' 
bundle install
```

##### 遇到提示 #1
```
Don't run Bundler as root. Installing your bundle as root will break this application for all non-root users on this machine.
```
如果有条件可以不用root就不用root

##### 遇到错误 #2
```
An error occurred while installing mysql2 (0.5.6), and Bundler cannot continue.
```

不使用mysql，忽略并重新配置

```
bundle config set --local without 'development test mysql2'
bundle install
```

##### 遇到错误 #3

```
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/3.1.0/gems/psych-5.2.2/ext/psych
/usr/bin/ruby3.1 -I /usr/lib/ruby/vendor_ruby -r ./siteconf20241222-35032-jkrt2z.rb extconf.rb
checking for yaml.h... no
yaml.h not found
```

```
apt install libyaml-dev
bundle install
```

#### 初始化数据库

```
RAILS_ENV=production bundle exec rake db:migrate
## 不建议用中文，有些初始数据无法翻译，还是英文较好
RAILS_ENV=production REDMINE_LANG="zh" bundle exec rake redmine:load_default_data
```

#### 运行

```
RAILS_ENV=production bundle exec rails server -e production
```


### Agile插件

- [redmine_agile-1_6_9-light.zip](https://www.redmine.org/plugins/redmine_agile)


### 如何通过git commit message来关闭问题

administration->settings->repositories->tracker

quick access:
```
http://localhost:3000/settings?tab=repositories
```
please use the your host:port
