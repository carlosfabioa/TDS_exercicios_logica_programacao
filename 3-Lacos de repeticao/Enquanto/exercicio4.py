'''
Ler um número N qualquer menor ou igual a 50 e apresentar o valor obtido 
da multiplicação sucessiva de N por 3 enquanto o produto for menor 
que 250 (N*3, N*3*3, N*3*3*3; etc)
'''

numero = int(input('Entre com um numero: '))

if numero < 50:
    while numero < 250:
        print(numero)
        numero = numero * 3
else:
    print('numero precisa ser menor que 50')
        