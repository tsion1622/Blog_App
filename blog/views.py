from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'title': 'blog post 1',
        'author': 'cory',
        'content': 'first content post',
        'date_posted': 'Auguest 17, 2018',
    },
     {
        'title': 'blog post 2',
        'author': 'tsi',
        'content': 'second content post',
        'date_posted': 'Auguest 27, 2018',
    }
]

def home(request):
    context = {
    'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')