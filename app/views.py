from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5