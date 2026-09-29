from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    html_header_and_title = "<h1>Selamat Datang di Blog Saya</h1>"
    return HttpResponse(html_header_and_title)

def get_blog_posts(request):
    blog_posts = Post.objects.all()
    return render(request, 'blogs/post_list.html', {'blog_posts': blog_posts})
