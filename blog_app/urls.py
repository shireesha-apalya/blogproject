from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='name'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('addpost/', views.post, name='add post'),
    path('blog/<int:pk>/', views.blog, name='blog post')
]
