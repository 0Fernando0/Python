'''
AGREGAÇÃO - POO
'''
from EX02B import CarrinhoDeCompra,Produto

carrinho = CarrinhoDeCompra()
p1 = Produto('camiseta',50)
p2 = Produto('calça',40)
p3 = Produto('meia',15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)

carrinho.lista_produtos()

print(carrinho.soma_total())



