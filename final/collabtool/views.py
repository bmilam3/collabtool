from django.shortcuts import render
from . models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'collabtool/home.html', context)


def about(request):
    return render(request, 'collabtool/about.html', {'title': 'About'})