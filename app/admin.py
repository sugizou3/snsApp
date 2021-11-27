from django.contrib import admin
from .models import Post, Comment, Friend, Tag, Good, Download

# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Tag)
admin.site.register(Good)
admin.site.register(Download)