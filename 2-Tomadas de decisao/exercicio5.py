'''
Ler dois valores numéricos e apresentar a diferença do maior para o menor
'''

a = float(input('Entre com o primeiro número: '))
b = float(input('Entre com o segundo número: '))

if a >= b:
    print('A diferença entre A e B é de ', a - b)
else:
    print('A diferença entre B e A é de ', b - a)