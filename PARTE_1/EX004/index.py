'''
script para detalhar o valor informado
'''

valor = input('digite algo: ')
print(f'''
o tipo primitivo desse valor é {type(valor)}
tem espaços? {valor.isspace()}
é um números? {valor.isnumeric()}
é um alfabetico? {valor.isalpha()}
é um alfanumerico? {valor.isalnum()}
esta em maiuscula? {valor.isupper()}
esta em minuscula? {valor.islower()}
esta capitalizada? {valor.istitle()}
''')
