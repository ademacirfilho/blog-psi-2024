from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo