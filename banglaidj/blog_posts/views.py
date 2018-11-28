from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'contact.html')

def all_posts(request):
    return render(request, 'all_posts.html')