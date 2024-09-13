from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    url = models.URLField(max_length=200)
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=30)
    url = models.URLField(max_length=150)
    imagem = models.ImageField()

    def __str__(self):
        return self.nome