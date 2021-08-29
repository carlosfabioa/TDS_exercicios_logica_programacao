'''
Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número 
lido como sendo um valor positivo, ou seja, o programa deverá apresentar o módulo 
de um número fornecido. Lembre-se de verificar se o número fornecido é menor que 
zero, sendo, multiplique-o por -1
'''

numero = float(input('Entre com um numero: '))

if( numero < 0):
    print('O módulo do número é: ', numero * -1)
else:
    print('O número digitado foi: ', numero)