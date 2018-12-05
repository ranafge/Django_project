from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()[::-1]
    return render(request, 'base.html', {'posts': posts})

def contact(request):
    return render(request, 'contact.html')

def all_posts(request):
    posts = Post.objects.all()[::-1]
    print(posts)
    return render(request, 'all_posts.html', {'posts':posts}, {'all_post': 'All post'})

def single_post(request, post_id):
    post= Post.objects.get(pk=post_id)
    return render(request, 'single_post.html', {'post': post}, {'page_title': 'Single post'})
