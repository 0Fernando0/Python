'''
script que diz se é verdadeiro ou falso (TRUE ou FALSE)
se tem SANTO na cidade informada
'''

cidade = str(input('em que cidade você nasceu? ')).upper().strip()
local = cidade.split()[0]
print('SANTO' in local)