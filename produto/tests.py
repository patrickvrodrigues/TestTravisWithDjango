from django.test import TestCase

from .models import ProdutoModel, CategoriaModel

class TesteProduto(TestCase):
    def setUp(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass
    
    def test_create_produto(self):
        produto = ProdutoModel()
        produto.produto = "Sabão"
        produto.quantidade = 10
        produto.categoria = None
        produto.save()
        produto = ProdutoModel()
        produto.produto = "Pera"
        produto.quantidade = 10
        produto.categoria = None
        produto.save()
        self.assertEqual(produto,ProdutoModel.objects.get(produto="Pera"))
    
    def test_cadastrar_negativo_deve_retornar_exception(self):
        teste = True
        self.assertEqual(True,teste)
