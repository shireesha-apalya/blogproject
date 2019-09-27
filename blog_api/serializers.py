from django.contrib.auth.models import User
from rest_framework import serializers
from blog_app.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = BlogPost
        fields = '__all__'
