class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self,produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for prod in self.produtos:
            print(prod.nome,prod.valor)

    def soma_total(self):
        total = 0
        for produt in self.produtos:
            total += produt.valor
        return total

class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor

    