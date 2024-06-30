from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'Yodit',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'June 29, 2024'
    },
{
        'author': 'Kaleab',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 30, 2024'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

