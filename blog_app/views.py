from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog_app.models import Contact, BlogPost
from blog_app.forms import ContactForm, BlogPostForm
from django.contrib.auth.models import User


def index(request):

    posts = BlogPost.objects.all()

    context = {"message": "welcome to index page !!!"}
    context["posts"] = posts
    return render(request, 'index.html', context)
    # return HttpResponseRedirect('/blog/')


def about_us(request):

    return render(request, 'about.html')


def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            p = Contact(name=name, contact=contact, email=email, message=message)
            p.save()
            return HttpResponseRedirect('/success/')


    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success(request):

    return render(request, 'success.html')


def post(request):

    if request.method == 'POST':

        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            author = form.cleaned_data['author']
            desc = form.cleaned_data['desc']
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            claps = form.cleaned_data['claps']
            p = BlogPost.objects.create(author=author,desc=desc, title=title, image=image,claps=claps)
            # p = BlogPost(desc=desc, title=title,image=image,created_date=created_date,updated_date=updated_date,claps=claps)
            p.save()
            return HttpResponseRedirect('/success/')


    else:
        form = BlogPostForm()

    return render(request, 'post.html', {'form': form})


def success(request):

    return render(request, 'success.html')

#
# def blog(request):
#
#     posts = BlogPost.objects.all()
#
#     context = {"message": "welcome to blog page !!!"}
#     context["posts"] = posts
#     return render(request, 'blog.html', context)

def blog(request,pk):
    post = BlogPost.objects.get(id=pk)
    context = {"post": post}
    return render(request, 'blog.html',context=context)