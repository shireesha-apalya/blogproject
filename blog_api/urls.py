from django.urls import path
from . import views


urlpatterns = [
    path('v1/home', views.home, name='name'),
    path('v1/blog-detail/<int:pk>', views.blog_detail)
]