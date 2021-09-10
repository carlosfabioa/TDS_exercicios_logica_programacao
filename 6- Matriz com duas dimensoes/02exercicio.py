'''
2.	Ler duas matrizes A e B, cada uma com uma dimensão para 7 elementos. 
Construir uma matriz C de duas dimensões, onde a primeira coluna deverá
 ser formada pelos elementos da matriz A e a segunda coluna deverá ser 
formada pelos elementos da matriz B
'''

LINHAS = 7

a=[]
b=[]
c=[]

#matriz A
print('Entre com os valores para matriz A')
for i in range(LINHAS):
	a.append(int(input('Entre com um numero: ')))

#matriz B
print('Entre com os valores para matriz B')
for i in range(LINHAS):
	b.append(int(input('Entre com um numero: ')))


for i in range(0,7):
    linha = []
    linha.append(a[i])
    linha.append(b[i])
    c.append(linha)

for i in c:
    print(i)
