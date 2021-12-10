from django.db import models
from django.db.models import fields
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView ,CreateView ,TemplateView
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import Post, Tag
from .forms import PostForm
import random, string

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
        'posts':post,
        'login_user':request.user,
    }

    return render(request, 'app/index.html',params)



class IndexView(ListView):
    model = Post
    template_name = 'app/index.html'
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.all().order_by('pub_data')


# モデルがないときに１度だけ実行すれば１００万件作成してくれる urlは/formssssss
class MakeData(TemplateView):
    """ユーザーの詳細ページ"""
    template_name = 'app/index.html'

    def get(self,request, **kwargs):
        context = super().get_context_data(**kwargs)

        for i in range(1000000):
            post = Post()
            post.main = 'test_' + str(i+1)
            post.bookname = 'test_' + str(i+1)
            post.author = 'test_' + str(i+1)
            post.sub = ''.join(random.choices(string.ascii_letters + string.digits, k=2000))
            post.owner = request.user
            post.save()

        return context




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
                






