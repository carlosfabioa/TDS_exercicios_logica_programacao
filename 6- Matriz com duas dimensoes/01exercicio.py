'''
1.	Ler duas matrizes A e B, cada uma de duas dimensões com 5 linhas e 3 colunas. 
Construir uma matriz C de mesma dimensão, onde C é formada pela soma dos elementos 
da matriz A com os elementos da matriz B
'''

LINHAS = 5
COLUNAS= 3
a = []
b = []
c = []

#matriz A
print('Entre com os valores para matriz A')
for i in range(LINHAS):
	linha = [] #cria alinha i
	for j in range(COLUNAS):
		linha.append(int(input('Entre com um numero: ')))
	a.append(linha)

print('Entre com os valores para matriz B')
#matriz B
for i in range(LINHAS):
	linha = [] #cria alinha i
	for j in range(COLUNAS):
		linha.append(int(input('Entre com um numero: ')))
	b.append(linha)

#matriz C
for i in range(LINHAS):
	linha = []
	c.append(linha)
	for j in range(COLUNAS):
		celula = a[i][j] + b[i][j]
		linha.append(celula)

for i in c:
    print(i)
