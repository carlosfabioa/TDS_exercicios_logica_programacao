'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer
 elevada a um expoente qualquer, ou seja, de NM
'''

base = int(input('Entre como valor da base: '))
potencia = int(input('Entre com o valor da potência: '))

resultado = 1
contador = 0

while contador < potencia: 
    resultado *=  base
    contador += 1
print(resultado)

