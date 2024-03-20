from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    altura = models.FloatField()
    largura = models.FloatField()
    profundidade = models.FloatField()

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()

    def __str__(self):
        return f'Comentário para {self.produto.nome}'
