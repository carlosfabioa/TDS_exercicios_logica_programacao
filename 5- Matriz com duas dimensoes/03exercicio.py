'''
3.	Ler 20 elementos para uma matriz qualquer, considerando que esta matriz tenha 
o tamanho de 4 linhas por 5 colunas
'''
LINHAS = 4
COLUNAS= 5
a = []

#matriz A
print('Entre com os valores para matriz A')
for i in range(LINHAS):
	linha = [] #cria alinha i
	for j in range(COLUNAS):
		linha.append(int(input('Entre com um numero: ')))
	a.append(linha)


for i in a:
    print(i)