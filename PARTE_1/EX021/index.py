'''
script que analisa o nome é apresenta
o nome em maiusculo, minusculo, quantas letras possui
'''

nome = input('Qual o Seu Nome completo: ')
print(f'''analisando seu nome
seu nome em maiusculo é {nome.upper()}
seu nome em minuscula é {nome.lower()}
seu nome tem ao todo {len(nome.replace(' ',''))}
seu primeiro nome é {nome.split()[0]} e ele tem {nome.find(' ')} letras
''')