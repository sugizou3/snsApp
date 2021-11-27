from django.db import models
from django.db.models import fields
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView ,CreateView

from .models import Post
from .forms import PostForm

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    ordering = ['-count_good']
    paginate_by = 5

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




