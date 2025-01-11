# Node install

```
# 设置https的代理，raw.githubusercontent.com被墙
export https_proxy=http://192.168.31.157:8082

pushd /tmp/
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
# Follow https://nodejs.org/en/download
nvm install 22

# 配置node mirror为科大mirror
export NVM_NODEJS_ORG_MIRROR=https://mirrors.ustc.edu.cn/node/
export NODE_MIRROR=https://mirrors.ustc.edu.cn/node/

```