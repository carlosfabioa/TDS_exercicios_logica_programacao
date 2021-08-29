'''
Apresentar os resultados de uma tabuada de um número qualquer. 
Esta deverá ser impressa no seguinte formato:
Considerando como exemplo o fornecimento do número 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
....
2 x 9 = 18
2 x 10 = 20
'''
#o usuário define qual tabuada será calculada
tabuada = int(input('Entre com a tabuada: '))
contador = 1

while contador <= 10:
    print (tabuada, ' X ', contador, ' = ', tabuada * contador)
    contador += 1