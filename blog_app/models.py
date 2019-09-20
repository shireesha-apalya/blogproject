from django.db import models
from django.conf import settings


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)


class Blog(models.Model):
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Desc = models.CharField(max_length=2000)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)


class Comment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_Desc = models.CharField(max_length=2000)
    created_date = models.DateField()


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Blog_category(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



