# django

## 编码约定

* 源文件的字符集使用utf8并声明

```python
# -*- coding:utf-8 -*-
```

* 源文件回车换行最好使用unix标准的*LR*



## 一些常用方法

#### 格式化日期字符串

```python
import datetime
time1 = datetime.datetime.strptime("2013-12-01 12:35:13.901426", "%Y-%m-%d %H:%M:%S.%f")
```

#### 获取当前日期

```python
import datetime
datetime.date.today()
```


## Django QuerySets里的**kwargs 动态创建ORM查询

bob_stories = Story.objects.filter(title__contains="bob", subtitle__contains="bob" ...)

bobargs = {"title_contains": 'bob', 'subtitle__contains': 'bob', 'text__contains': 'bob', 'byline__contains': 'bob'}
bob_stories = Story.objects.filter(**bobargs)

bobargs = dict((f+'__contains', 'bob') for f in ('title', 'subtitle', 'text', 'byline'))
bob_stories = Story.objects.filter(**bobargs)

## 使用七牛云存储

picture = models.ImageField(_('scene picture'), max_length=256, storage=QiniuStorage())