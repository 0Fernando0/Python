"""
4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?  

IMPORTANTE:  

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.  

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)  

c) Explique como chegou no resultado. 
"""

"""
R : o carro está mais próximo da cidade de Ribeirão Preto no momento em que os dois veículos se cruzam.

Para responder a pergunta, precisa calcular a distância percorrida pelo carro e pelo caminhão até o momento em que eles se encontram na rodovia.

a distância entre Ribeirão Preto e Franca é de 100 km. os veículos estão se movendo em direções opostas, a distância percorrida pelo carro e pelo caminhão é a soma das distâncias de cada veículo até o ponto de encontro. Podemos fazer distância = velocidade x tempo.

o carro está se movendo a uma velocidade constante de 110 km/h. Como a distância entre as cidades é de 100 km, podemos calcular o tempo que o carro leva para percorrer essa distância dividindo a distância pela velocidade: tempo = distância/velocidade = 100/110 = 0,91 horas. No entanto, o carro tem uma tag de pedágio e não precisa parar então não precisa considerar o tempo gasto em pedágios.

o caminhão está se movendo a uma velocidade constante de 80 km/h e leva 5 minutos a mais em cada pedágio. o caminhão precisa passar por dois pedágios no caminho. então, o tempo que o caminhão leva para percorrer a distância entre as cidades é o tempo que leva para percorrer a distância de 100 km a uma velocidade de 80 km/h, mais o tempo gasto nos pedágios. 100/80 = 1,25 horas. Como o caminhão leva 5 minutos a mais em cada pedágio, o tempo total gasto nos pedágios é de 10 minutos = 0,17 horas. logo, o tempo que o caminhão leva para percorrer a distância entre as cidades é de 1,25 + 0,17 = 1,42 horas.

A distância percorrida pelo caminhão até o ponto de encontro é 80 x 1,42 = 113,6 km.

o ponto de encontro fica a meio caminho entre as duas cidades. Portanto, a distância do ponto de encontro até Ribeirão Preto é de 50 km. Comparando as distâncias percorridas pelo carro e pelo caminhão, podemos ver que o carro percorreu uma distância menor até o ponto de encontro (100 km), enquanto o caminhão percorreu uma distância maior (113,6 km).
"""