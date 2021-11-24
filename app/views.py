from django.db import models
from django.db.models import fields
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import PostForm

from app.forms import PostForm
from .models import Post

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

def CreateView(request):
    if (request.method == 'POST'):
        obj = Post()
        post = PostForm(request.POST, instance=obj)
        post.save()
        return redirect(to='')
    return render(request,'app/create.html')
