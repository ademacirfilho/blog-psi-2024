from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, "index.html")

def blog(request):
    posts = Post.objects.all()
    
    context = {
        "posts": posts,
    }
    return render(request, "blog.html", context)

def contact(request):
    return render(request, "contact.html")

def post(resquest):
    return render(resquest, "post.html")