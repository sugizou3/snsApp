from django.db import models
from django.db.models import fields
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView ,CreateView
from django.http import JsonResponse

from .models import Post, Tag
from .forms import PostForm

# Create your views here.
def index(request):
    user = request.user
    tags = Tag.objects.filter(owner=user)
    
    if request.method =='POST':
        # print(tags[0].tag)
        # print(request.POST['javascript'])
        # post = Post.objects.all
        for tag in tags:
            if tag.tag in request.POST:
                print(tag)
                post = Post.objects.filter(main = tag)
        # if request.POST['search']:
        #     word_search=request.POST['search']
        #     post = Post.objects.filter(main = word_search)


    else:
        post = Post.objects.all

    print('aaqqqqqqaaa')
    
    params = {
        'tags':tags,
        # 'posts':post,
        'login_user':request.user,
    }

    return render(request, 'app/index.html',params)




def form(request):
    if request.method == 'POST':
        post = Post()
        post.main = request.POST['main']
        post.bookname = request.POST['bookname']
        post.author = request.POST['author']
        post.sub = request.POST['sub']
        post.owner = request.user
        post.save()
        return redirect(to='/')
    return render(request, 'app/create.html')


def ajax_search(request):
    print('qqqq')
    keyword = request.POST.get('keyword')
    print(keyword)
    # 検索キーワードがあればそれで絞り込み、なければ全ての記事
    # JSONシリアライズするには、Querysetをリストにする必要あり
    if keyword:
        posts = Post.objects.filter(main = keyword)  # タイトルにキーワードを含む。大文字小文字の区別なし
        data = [PostMapper(post).as_dict() for post in posts]
    else:
        posts = Post.objects.all
        data = [PostMapper(post).as_dict() for post in posts]
    print(data)
    

    # d = {
    #     'posts': posts,
    # }
    return JsonResponse(data,safe=False)

class PostMapper:
    def __init__(self, obj):
        self.obj = obj  

    def as_dict(self):
        return {
            'owner': self.obj.owner.username,
            'main': self.obj.main,
            'bookname': self.obj.bookname,  
            'author': self.obj.author,  
            'sub': self.obj.sub,  
            'count_good': self.obj.count_good,  
            'comment': self.obj.comment,  
            'pub_data': self.obj.pub_data,
        }  
                






