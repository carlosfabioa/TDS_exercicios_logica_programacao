'''
5.	Ler duas matrizes A e B, cada uma com uma dimensão para 12 elementos. 
Construir uma matriz C de duas dimensões, onde a primeira coluna da matriz 
C deverá ser formada pelos elementos da matriz A multiplicados por 2, e a 
segunda coluna deverá ser formada pelos elementos da matriz B subtraídos de 5.
'''

LINHAS = 12

a = []
b = []
c = []

#matriz A
print('Entre com os valores para matriz A')
for i in range(LINHAS):
	a.append(int(input('Entre com um numero: ')))

#matriz B
print('Entre com os valores para matriz B')
for i in range(LINHAS):
	b.append(int(input('Entre com um numero: ')))

#Matriz C
for i in range(0,LINHAS):
    linha = []
    linha.append(a[i] * 2)
    linha.append(b[i] - 5)
    c.append(linha)

for i in c:
    print(i)