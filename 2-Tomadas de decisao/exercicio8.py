'''
Efetuar a leitura de quatro números inteiros e apresentar os números que não são divisíveis por 2 e 3
'''
numero1 = int(input('Entre com o primeiro numero: '))
numero2 = int(input('Entre com o segundo numero: '))
numero3 = int(input('Entre com o terceiro numero: '))
numero4 = int(input('Entre com o quarto numero: '))

print('NÃO SÃO DIVISIVEIS POR 2: ')
if numero1 % 2 != 0:
    print(numero1)
if numero2 % 2 != 0:
    print(numero2)
if numero3 % 2 != 0:
    print(numero3)
if numero4 % 2 != 0:
    print(numero4)


print('NÃO SÃO DIVISIVEIS POR 3: ')
if numero1 % 3 != 0:
    print(numero1)
if numero2 % 3 != 0:
    print(numero2)
if numero3 % 3 != 0:
    print(numero3)
if numero4 % 3 != 0:
    print(numero4)