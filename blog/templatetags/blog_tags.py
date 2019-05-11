from django import template
from ..models import Post, Category

# 实例化了一个 template.Library 类
register = template.Library()

# 通过 register = template.Library() 和 @register.simple_tag 装饰器将函数装饰为一个模板标签。
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()

