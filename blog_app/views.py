from django.shortcuts import render


def index(request):
    context = {"message": "welcome to index page !!!"}
    return render(request, 'index.html', context)

