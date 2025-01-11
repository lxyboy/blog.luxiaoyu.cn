#VDIStack 平台开发框架设计

## 1. 支持app形式应用可插拔

app形式为一个app_name的包，以app_name为名字为目录，结构如下

```txt
|app_name/
|----__init__.py
|----views.py
|----models.py
|----other_source.py
|----...
```

**把这样的目录放置在apps下就能够被系统识别，并可以通过以app_name开头的url进行访问**
务必确保包含```views.py```,这个是这个包识别的入口
下面是一个views.py的简单例子

```python
# -*- coding:utf-8 -*-
from flask import Blueprint
# 这里的名字请不要修改，采用包名
import models
app = Blueprint(__package__.split('.')[-1], __name__)


@app.route('/')
def function1():
    return 'app2 function1'


@app.route('/function2')
def function2():
    return 'app2 function2'
```

## 2.关于多语言机制(使用Flask-babel) TODO根据浏览器，或者用户配置自动选择


**Flask-babel发现translations的路径为与Flaskapp初始化时的路径下的可以通过查看babel中get_translations函数来调试** **如果不注意Flask app初始化的位置，这个问题是大坑**

在app中多国语言使用方法

```python
from flask.ext.babel import _

@app.route('/')
def index():
    return _('function2')
```

创建

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l zh_Hans_CN
pybabel compile -d translations
```

可以先编辑messages.pot模板然后执行init，进入translations翻译，然后编译translations

更新

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
pybabel compile -d translations
```

在进行compile前先对translations中的po文件进行翻译，去除fuzzy


## 3.关于Flask-Script脚本 类似 django manage.py

使用 ```python manage.py --help``` 查看用法

添加命令参考manage.py文件


## 4.关于数据库支持 Flask-SQLAlchemy sqlalchemy-migrate

**鉴于sqlalchemy-migrate的BUG多更改为使用alembic**

配置alembic.ini设置其中的数据库连接*sqlalchemy.url*



```
# 自动生成版本
alembic revision --autogenerate -m "your message"
# 数据库升级
alembic upgrade head
```

migrate仅限制与添加删除字段，不会重命名字段，再者必须确保迁移生成的脚本是正确的，最后在没有备份的情况下不要去迁移数据库，当然也不要在生产环境迁移。

**Flask-SQLAlchemy创建表名为group时出问题（sqlite数据库）（'表名为特殊名字'）**

```bash
#创建数据库表
python manage.py db_create
#migrate创建的数据库表
python manage.py db_migrate
#升级数据库表
python manage.py db_upgrade
#返回上一次数据库表
python manage.py db_rollback
#删除数据库表和migrate 危险～请备份
python manage.py db_delete
```

## 5. Restful风格 API实现

1.通过JZMethodView类化method调用

```python
from utils.jzviews import JZMethodView
class UserAPI(JZMethodView):
    def post(self, user_id=None):
        return ""
    def get(self, user_id=None):
        return ""
    # ... Http Method (get|post|delete|put)
# 添加url规则
api.add_resource(UerAPI, 'users', '/users/<int:user_id>/'
```

2.实现JZResource类完成models的dict化

```python
from utils.jzresource import JZResource
from vdistack import db
# 继承JZResource后即可直接在JZMethodView的方法中返回该类实例而无需进行序列化
class JZUser(db.Model, JZResource):
    __tablename__ = 'jzuser'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), index=True, unique=True)
```

## 6. 测试框架


测试命令```python vdistack_tests.py```

测试框架例子测试代码

```python
# 参数格式可以参考werkzeug/test.py EnvironBuilder
def test_add_group(self):
    rv = self.client.put('/app1/groups',
                         content_type='application/json',
                         data='''{"name": "group1"}''',
                         follow_redirects=True)
    assert "name" in rv.data
```

## 7. 关于部署和开发环境

使用配置文件为settings.py 分3总模式的配置

1. development
2. testing
3. production

## 环境变量
1.密钥
VDISTACK_SECRET_KEY
2.VDISTACK的配置选项
VDISTACK_FLASK_CONFIG

## TODO
1. 添加分页

sudo apt-get install libssl-dev
sudo apt-get install libffi-dev