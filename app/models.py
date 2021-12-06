from django.core.checks import messages
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User



class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_owner')
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.comment


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_owner')
    main = models.TextField(max_length=300)
    bookname = models.TextField(max_length=50)
    author = models.TextField(max_length=50)
    sub = models.TextField(max_length=1000)
    count_good = models.IntegerField(default=0)
    comment = models.IntegerField(default=-1)
    pub_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.main)
    
    def get_share(self):
        return Post.objects.get(id=self.comment.id)
    
    class Meta:
        ordering = ('-pub_data',)


class PostMapper:
    def __init__(self, obj):
        self.obj = obj  

        def as_dict(self):
            return {
                'owner': self.obj.owner,
                'main': self.obj.main,
                'bookname': self.obj.bookname,  
                'author': self.obj.author,  
                'sub': self.obj.sub,  
                'count_good': self.obj.count_good,  
                'comment': self.obj.comment,  
                'pub_data': self.obj.pub_data,
            }  


class Friend(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='friend_owner')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='friend_user')

    def __str__(self):
        return str(self.owner) 

class Tag(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tag_owner')
    tag = models.TextField(max_length=20)

    def __str__(self):
        return str(self.tag)

class Good(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='good_owner')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='good_user')

    def __str__(self):
        return str(self.owner)

class Download(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='download_user')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='download_post')


