from django import forms
from .models import UploadedFile
from django.db import models
from.models import Blog
class BlogPost(form.ModelForm): 
    class Meta: 
        model = Blog 
        fields = ['title','body']
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)