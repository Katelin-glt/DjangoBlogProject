
from django.conf.urls import url

from . import views

# 给这个评论的URL模式规定命名空间
app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]