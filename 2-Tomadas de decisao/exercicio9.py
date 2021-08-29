'''
Efetuar a leitura de cinco números inteiros e identificar o maior e o menor valor.
'''
numero1 = int(input('Entre com o primeiro numero: '))
numero2 = int(input('Entre com o segundo numero: '))
numero3 = int(input('Entre com o terceiro numero: '))
numero4 = int(input('Entre com o quarto numero: '))
numero5 = int(input('Entre com o quinto numero: '))

if numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5:
    print('\nO maior número é o numero: ', numero1)
if numero2 > numero1 and numero2 > numero3 and numero2 > numero4 and numero2 > numero5:
    print('\nO maior número é o numero: ', numero2)
if numero3 > numero1 and numero3 > numero2 and numero3 > numero4 and numero3 > numero5:
    print('\nO maior número é o numero: ', numero3)
if numero4 > numero1 and numero4 > numero2 and numero4 > numero3 and numero4 > numero5:
    print('\nO maior número é o numero: ', numero4)
if numero5 > numero1 and numero5 > numero2 and numero5 > numero3 and numero5 > numero4:
    print('\nO maior número é o numero: ', numero5)

if numero1 < numero2 and numero1 < numero3 and numero1 < numero4 and numero1 < numero5:
    print('\nO menor número é o numero: ', numero1)
if numero2 < numero1 and numero2 < numero3 and numero2 < numero4 and numero2 < numero5:
    print('\nO menor número é o numero: ', numero2)
if numero3 < numero1 and numero3 < numero2 and numero3 < numero4 and numero3 < numero5:
    print('\nO menor número é o numero: ', numero3)
if numero4 < numero1 and numero4 < numero2 and numero4 < numero3 and numero4 < numero5:
    print('\nO menor número é o numero: ', numero4)
if numero5 < numero1 and numero5 < numero2 and numero5 < numero3 and numero5 < numero4:
    print('\nO menor número é o numero: ', numero5)