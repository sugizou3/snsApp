from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    username_post = models.ForeignKey(User,on_delete=models.CASCADE)
    main = models.TextField()
    author = models.TextField()
    sub = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.main
