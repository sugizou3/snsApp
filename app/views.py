from django.db import models
from django.db.models import fields
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView ,CreateView

from .models import Post, Tag
from .forms import PostForm

# Create your views here.
def index(request):
    user = request.user
    tags = Tag.objects.filter(owner=user)
    
    if request.method =='POST':
        for tag in tags:
            if request.POST[str(tag)]:
                post = Post.objects.filter(main = tag)
        if request.POST['search']:
            word_search=request.POST['search']
            post = Post.objects.filter(main = word_search)


    else:
        post = Post.objects.all
    
    params = {
        'tags':tags,
        'posts':post,
        'login_user':request.user,
    }

    return render(request, 'app/index.html',params)





class IndexView(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    ordering = ['-count_good']

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




