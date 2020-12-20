from django.db import models

class CategoriaModel(models.Model):
    categoria = models.CharField(max_length=40)

class ProdutoModel(models.Model):
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.SET_NULL, null=True)
    produto = models.CharField(max_length=40)
    quantidade = models.PositiveIntegerField()
