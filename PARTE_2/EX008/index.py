peso = float(input('Quanto Você Pesa? (Kg)'))
altura = float(input('Qual A Sua Altura? (m)'))
imc = peso / (pow(altura,2))
print('seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está com Peso ideal')
elif imc >= 25 and imc < 30:
    print('você esta com o peso acima da média')
elif imc >= 30 and imc <40:
    print('Você está em obesidade')
else:
    print('Obesidade Morbida')
