
from django import forms
from .models import Comment

# Django 的表单类必须继承自 forms.Form 类或者 forms.ModelForm 类
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # 表明这个表单对应的数据库模型是 Comment 类
        fields = ['name', 'email', 'url', 'text'] # 指定了表单需要显示的字段


