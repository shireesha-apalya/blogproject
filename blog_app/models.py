from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=2000)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    claps = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_Desc = models.CharField(max_length=2000)
    created_date = models.DateField()


class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=50)

