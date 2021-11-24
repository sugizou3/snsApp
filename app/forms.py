from django import forms
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['username_post', 'main', 'bookname', 'author', 'sub', 'date_posted']