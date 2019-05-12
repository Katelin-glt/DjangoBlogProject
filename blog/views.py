from django.shortcuts import render
# coding: utf-8
# Create your views here.

import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm

# request是Django为我们封装好的HTTP请求，是类HttpRequest的一个实例
def index(request):

    """
    # 返回一个HTTP相应给用户，HTTP响应也是Django帮我们封装好的，是类HttpResponse的一个实例，只是我们给它传了一个自定义的字符串参数
    return HttpResponse("欢迎访问我的博客首页！")

    # render函数根据传入的参数来构造HttpResponse
    # 1.首先把 HTTP 请求传了进去
    # 2.render 根据第二个参数的值 blog/index.html 找到这个模板文件并读取模板中的内容
    # 3.render 根据我们传入的 context 参数的值把模板中的变量替换为我们传递的变量的值
    # 4.HTML 模板中的内容字符串被传递给 HttpResponse 对象并返回给浏览器(Django 在 render 函数里隐式地帮我们完成了这个过程）
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
    """

    # - 号表示逆序，如果不加 - 则是正序
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    # 当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post
    # 如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
    post = get_object_or_404(Post, pk=pk)
    # 阅读量 +1
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }

    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

