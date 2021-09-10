'''
4.	Ler uma matriz A de uma dimensão com 10 elementos. Construir uma matriz C 
de duas dimensões com três colunas, onde a primeira coluna da matriz C é formada
pelos elementos da matriz A somados com mais 5, e a segunda coluna é formada pelo 
valor do cálculo do fatorial de cada elemento correspondente da matriz A e a 
terceira e última coluna deverá ser formada pelos quadrados dos elementos
correspondente da matriz A.
'''

LINHAS = 10

def fatorial(n):
    fatorial = 1
    for contador in range(1,n+1):
        fatorial *= contador
    return fatorial

a = []
c = []

#matriz A
print('Entre com os valores para matriz A')
for i in range(LINHAS):
	a.append(int(input('Entre com um numero: ')))

#Matriz C
for i in range(0,LINHAS):
    linha = []
    linha.append(a[i] + 5)
    linha.append(fatorial(a[i]))
    linha.append(a[i] * a[i])
    c.append(linha)

for i in c:
    print(i)