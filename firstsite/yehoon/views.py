from .models import Blog
from django.shortcuts import render, get_object_or_404
from .form import BlogPost
from .models import Photo
from django.views.generic import ListView
from .forms import FileUploadForm
# Create your views here.

def lion(request):
    blogs = Blog.objects
    return render(request, 'blog/lion.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})
def blogpost(request): 
    if request.method == "POST": 
        form = BlogPost(request.POST) 
        if form.is_valid(): 
            post = form.save(commit=False)
            post.pub_date=timezone.now() 
            post.save() 
            return redirect('home')
    else: 
        form = BlogPost()
        return render(request,'new.html',{'form':form})

class PhotoListView(ListView):
    model = Photo
    template_name = 'photo_list.html'
    context_object_name = 'photos'


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'fileupload/upload_file.html', {'form': form})

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'fileupload/file_list.html', {'files': files})