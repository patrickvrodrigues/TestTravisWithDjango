from django.contrib import admin
from .models import ProdutoModel, CategoriaModel

# Register your models here.
admin.site.register(ProdutoModel)
admin.site.register(CategoriaModel)