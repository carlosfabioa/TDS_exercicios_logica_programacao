'''
Efetuar a leitura de três valores (variáreis A, B, C) e efetuar o cálculo 
da equação de segundo grau, apresentando as duas raízes, se para os valores
informados for possível efetuar o referido cálculo
'''

a = int(input('Entre como primeiro número: '))
b = int(input('Entre como segundo número: '))
c = int(input('Entre como terceiro número: '))



if a == 0:
    print('Não podemos ter A como zero, pois não é possível dividir um numero por zero')
    a = int(input('Entre com novamente com o valor de A: '))
delta = b**2 - 4 * a * c


if delta < 0:
    print("não tem raizes reais")
elif delta == 0:
    x = b / 2*a
    print('As duas raizes reais são iguais x1 e x2= ', x)
elif delta > 0:
    x1 = (-b + delta**0.5 )/ 2*a
    x2 = (-b - delta**0.5 )/ 2*a
    print('x1= ', x1)
    print('x2=', x2)

