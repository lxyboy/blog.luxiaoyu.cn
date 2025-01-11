web开发

### validator

### 装饰器

```
def login_required(func, permissions=[], redirect_view_name="account:login"):
    @functools.wraps(func)
    def _login_required(request, *args, **kwargs):
        user = request.user
        if user is None:
            return redirect(reverse(redirect_view_name))
        else:
            has_permission, no_permission = request.user.has_permissions(permissions)
            if has_permission:
                return func(request, *args, **kwargs)
            else:
                return redirect(reverse(redirect_view_name))
    return _login_required
```
	
	
### 关于jquery的attr设置

```
function submitForm(formID, actionPath){
	$("#"+formID).attr("action", actionPath);
	$("#"+formID).submit();
}
```


### django分页

```
    page_number = dl_utils.str2int(request.GET.get("page_number", 1), 1)
    page_per_page = dl_utils.str2int(request.GET.get("page_per_page", 20), 20)
    order_status = request.GET.getlist("order_status", ['1', '2', '3'])

    orders_list = Order.objects.filter(status__in=order_status).filter(group=request.user.group)
    paginator = Paginator(orders_list, page_per_page)

    try:
        orders = paginator.page(page_number)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
```

### django ForeignKey

```
shop_group = models.ForeignKey(DLGroup, related_name="shop_group", verbose_name=u"拍摄机构", null=True)
postproduction_group = models.ForeignKey(DLGroup, related_name="postproduction_group", verbose_name=u"后期机构", null=True)
admin_group = models.ForeignKey(DLGroup, related_name="admin_group", verbose_name=u"管理机构", null=True)
```

### django filter
date:'Y-m-d H:i:s'
date:'Y-m-d H:i'


### django escape {{ and }}

<p>"{% templatetag openvariable %} some text {% templatetag closevariable %}"</p>


### django complex query
http://192.168.1.14/docs/django1.8/topics/db/queries.html


### django media文件

在部署环境问题好解决，直接在nginx中配置statc、media两个文件夹静态访问即可。

在开发环境中，经常会碰到这两个文件夹里面的内容无法访问，STATIC_ROOT、STATIC_URL、MEDIA_ROOT被搞的晕晕的，下面的方法可以解此困局

第一步：
打开总配置目录下的urls.py，比如mysite/urls.py，添加下面内容
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )

第二步：
打开总配置目录下的settings.py，比如mysite/settings.py，添加下面内容
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

OK，这样就可以在浏览器中访问http://127.0.0.1:8000/static/xxx 或 http://127.0.0.1:8000/media/xxx 了