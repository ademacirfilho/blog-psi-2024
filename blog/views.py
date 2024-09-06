from django.shortcuts import render
from .models import Post, Noticia, Pessoa

def index(request):
    noticias = Noticia.objects.all()

    context = {
        "noticias": noticias
    }
    
    return render(request, "index.html", context)

def blog(request):
    posts = Post.objects.all()
    
    context = {
        "posts": posts,
    }
    return render(request, "blog.html", context)

def contact(request):
    pessoas = Pessoa.objects.all()

    context = {
        "pessoas": pessoas    
        }
    return render(request, "contact.html", context)

def post(resquest):
    return render(resquest, "post.html")