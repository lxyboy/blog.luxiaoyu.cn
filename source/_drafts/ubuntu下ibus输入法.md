## 关于linux下输入法

在ubuntu下安装中文输入法

### 查看可用的ibus中文输入法

```bash
apt-cache search ibus | grep pinyin
```

> ibus-pinyin - Pinyin engine for IBus
> ibus-sunpinyin - sunpinyin engine for ibus
> ibus-googlepinyin - googlepinyin engine for ibus
> ibus-libpinyin - Intelligent Pinyin engine based on libpinyin for IBus
> pinyin-database - PinYin database used by ibus-pinyin

### 安装和配置ibus

```bash
apt-get install ibus-libpinyin
ibus-setup
```

*ibus-setup* 可以配置ibus的相关信息.

**注意:** 别忘记设置Text Entry Settings(右键输入法图标,配置input source use选项)


### ibus-pinyin不推荐

每次使用这个输入法都会有错误，不知道是什么原因～

### ibus-sunpinyin不推荐

这个输入法在输入类似**xuexi**这样的**ue**这个音的时候会出现错误。

### ibus-googlepinyin 可以使用

这个输入法是google的引擎。感觉还可以

### ibus-libpinyin 推荐

好用~一直在用~