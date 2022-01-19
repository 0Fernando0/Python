from EX03B import Endereco,Cliente

c1 = Cliente('Fernando',21)
c1.inserir_endereco('Rio De Janeiro','RJ')
print()

c2 = Cliente('Anderson',39)
c2.inserir_endereco('belo horizonte','MG')

print(c1.nome)
c1.lista_endereco()
print(c2.nome)
c2.lista_endereco()
