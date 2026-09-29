from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import ContactForm
from .models import Post, ContactMessage

def home(request):
    html_header_and_title = "<h1>Selamat Datang di Blog Saya</h1>"
    return HttpResponse(html_header_and_title)

def get_blog_posts(request):
    blog_posts = Post.objects.all()
    return render(request, 'blogs/post_list.html', {'blog_posts': blog_posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogs/post_detail.html', {'post': post})


class ContactView(CreateView):
    template_name = "blogs/contact.html"
    form_class = ContactForm
    model = ContactMessage
    success_url = reverse_lazy("contact_thanks")

class ContactThanksView(TemplateView):
    template_name = "blogs/contact_thanks.html"
