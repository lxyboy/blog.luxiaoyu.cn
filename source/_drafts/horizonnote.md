# horizon可插拔的dashboard分析

#### openstack_dashboard/settings.py

设定url的入口

```python
ROOT_URLCONF = 'openstack_dashboard.urls' #设定入口urls
```

下面的代码很关键，是horizon的dashboard配置选项，打开或者关闭dashboard的开关，同时也为后面的_autodiscover()函数提供配置 **这部分可能需要确认，虽然没有仔细看，但是应该不会错**

```python
INSTALLED_APPS = list(INSTALLED_APPS)  # Make sure it's mutable
settings.update_dashboards([
    openstack_dashboard.enabled,
    openstack_dashboard.local.enabled,
], HORIZON_CONFIG, INSTALLED_APPS)
```

#### openstack_dashboard/urls.py

```python
import horizon # 导入horizon

# ...

    url(r'', include(horizon.urls)) #设定可访问的urls
``` 

导入horizon时执行 horizon/__init__.py

####  horizon/__init__.py

```python
    from horizon.base import Dashboard  # noqa 
    from horizon.base import Horizon  # noqa 
    from horizon.base import Panel  # noqa 
    from horizon.base import PanelGroup  # noqa
    
    urls = Horizon._lazy_urls  # urls为上面使用的urls
    
__all__ = [
    #...
    "urls",
]  # import horizon时导入的符号 声明上面的urls     
```

#### horizon/base.py

```python
Horizon = HorizonSite() #HorizonSite是Site类的单例模式实现

class Site(Registry, HorizonComponent): # Site类继承自Registry和HorizonComponent

    @property
    def _lazy_urls(self):  # 访问的就是这个url
        def url_patterns():
            return self._urls()[0]    # 调用该函数生成urls  
    return LazyURLPattern(url_patterns), self.namespace, self.slug
```

Site下的_urls()函数一

```python
urlpatterns = self._get_default_urlpatterns() # 主要执行了 import_module('.horizon.site_urls', 'horizon')
self._autodiscover() #该函数相对比较复杂，自我发现一些urlpattern
```

Site下的_autodiscover()函数

```python
        # Discover both dashboards and panels, in that order
        for mod_name in ('dashboard', 'panel'):  
            for app in settings.INSTALLED_APPS:
                mod = import_module(app)
                try:
                    before_import_registry = copy.copy(self._registry)
                    import_module('%s.%s' % (app, mod_name))
                except Exception:
                    self._registry = before_import_registry
                    if module_has_submodule(mod, mod_name):
                        raise
    #对INSTALLED_APPS下的进行模块的导入这里主要针对的openstack_dashboard这个模块 1. mod_name 为 'dashboard' 时 导入类似 import_module('openstack_dashboard.dashboards.*.dashboard')
    # 这里就可以导入openstack_dashboard.dashboards.admin下dashboard.py文件了，该文件完成注册dashboard的功能
```
Site下_urls函数二 发现dashboard下的panel

```python
        for dash in self._registry.values():
            dash._autodiscover()
            
        self._load_panel_customization()
        
        #生成动态的 urlconf
        for dash in self._registry.values():
            urlpatterns += patterns('',
                                    url(r'^%s/' % dash.slug,
                                        include(dash._decorated_urls)))        
```

##### horizon/site_urls.py

主要处理 '^home/$' 这个urlpatterns
另外 载入一些js处理的url

##### openstack_dashboard/dashboards/admin/dashboard.py

```python
#该句完成的Dashboard的注册工作
horizon.register(Admin)
```

