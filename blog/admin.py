from django.contrib import admin

from .models import Post, Noticia, Pessoa

admin.site.register(Post)
admin.site.register(Noticia)
admin.site.register(Pessoa)