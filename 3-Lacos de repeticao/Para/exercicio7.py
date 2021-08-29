'''
Elaborar um programa que apresente o valor de uma potência de uma base 
qualquer elevada a um expoente qualquer, ou seja, NM
'''

base = int(input('Entre como valor da base: '))
potencia = int(input('Entre com o valor da potência: '))

resultado = 1

for i in range( potencia): 
    resultado *=  base
print(resultado)