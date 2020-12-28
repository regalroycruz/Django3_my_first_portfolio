from django.shortcuts import render, get_object_or_404
from . models import Blog

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def all_blogs(request):
    # return render(request, 'blog/home.html')
    blogs=Blog.objects.all()
    return render(request, 'blog/home.html', {'blog':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'id':blog})