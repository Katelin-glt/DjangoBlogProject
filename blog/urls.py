
from django.conf.urls import url  # 导入url函数
from . import views  # 从当前目录下导入views模块

#  告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间。

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 当用户访问 <网站域名>/post/1/ 时，显示的是第一篇文章的内容
    # (?P<pk>[0-9]+) 表示命名捕获组，其作用是从用户访问的 URL 里把括号内匹配的字符串捕获并作为关键字参数传给其对应的视图函数 detail。
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]


