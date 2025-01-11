Docker

```bash
sudo apt-get update
sudo apt-get install docker.io
```

Then, to enable tab-completion of Docker commands in BASH, either restart BASH or

```bash
source /etc/bash_completion.d/docker.io
```

从官网拉官方映像

由于中国存在GFW，可以翻墙，或者尝试
修改host文件：

```txt
54.234.135.251  get.docker.io
54.234.135.251  cdn-registry-1.docker.io
```

```
sudo docker.io pull ubuntu
```

使用docker列出所有docker images

```
sudo docker.io images
```

```
sudo docker.io ps #查看当前运行的container
sudo docker.io ps -a #查看所有的container
sudo docker.io ps -a -q #仅仅列出container数字id
sudo docker.io rm # 删除container
sudo docker.io rmi # 删除image
sudo docker.io rm `sudo docker.io ps -a -q` #删除所有container
```

执行一次

```
sudo docker.io run ubuntu /bin/echo 'Hello world' # 启动一个container运行/bin/echo命令显示'hello world',但是container未被删除
sudo docker.io --rm=true run ubuntu /bin/echo "hello world" # 启动一个container运行/bin/echo命令 结束后删除自己
```


