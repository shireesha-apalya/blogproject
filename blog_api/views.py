from django.shortcuts import render

from blog_api.serializers import BlogPostSerializer
from blog_app.models import BlogPost
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view


# def home(request):
#     blogs = BlogPost.objects.all()
#     print("welocme",blogs)
#     blogs_list = []
#     for blog in blogs:
#         print("&&&", blog)
#         blog_obj = {
#             "id":blog.id,
#             'author':blog.author.username,
#             'title':blog.title,
#             'desc':blog.desc,
#             'image':str(blog.image),
#             'claps':blog.claps
#         }
#         blogs_list.append(blog_obj)
#     print("hello",blogs_list)
#     resp = {
#         "status":"success",
#         "code":200,
#         "message":"success",
#         "results":blogs_list
#     }
#     blog_json = json.dumps(resp, indent=2)
#     return HttpResponse(blog_json)

@api_view(['GET'])
def home(request):
    if request.method == "GET":
        blogs = BlogPost.objects.all()
        blog_serializer = BlogPostSerializer(blogs,many=True)
        return Response(blog_serializer.data)

@api_view(['GET'])
def blog_detail(request,pk):
    if request.method == "GET":
        blog = BlogPost.objects.get(id=pk)
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)