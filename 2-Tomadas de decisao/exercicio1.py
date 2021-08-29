'''
Efetuar a leitura de três valores (variáveis A, B e C) e apresentar 
os valores dispostos em ordem crescente
'''

a = int(input('Entre com o primeiro número: '))
b = int(input('Entre com o segundo número: '))
c = int(input('Entre com o terceiro número: '))

if a < b and b < c:
    print(a, b, c)
elif a < b and b > c and a < c:
    print(a, c, b)
elif a < b and b > c and a > c:
    print(c, a, b)

if a > b and b < c and a < c:
    print(b, a, c)
elif a > b and b < c and a > c:
    print(b, a, c)
elif a > b and b > c:
    print(c, b, a)