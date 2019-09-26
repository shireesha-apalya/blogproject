from django import forms
from django.contrib.auth.models import User
from blog_app.models import BlogPost
class ContactForm(forms.Form):
  name = forms.CharField(label='Your Name', max_length=100)
  contact = forms.CharField(label='Phone Number', max_length=10, min_length=10)
  email = forms.CharField(label='email', max_length=20)
  message = forms.CharField(label='message', max_length=50)
#
#
# class BlogPostForm(forms.Form):
#   author = forms.CharField(max_length=10)
#   desc = forms.CharField(max_length=2000)
#   title = forms.CharField(max_length=50)
#   image = forms.ImageField()
#   created_date = forms.DateField()
#   updated_date = forms.DateField()
#   claps = forms.IntegerField()
#

# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()
class BlogPostForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = "__all__"