'''
g.	Ler 20 elementos de uma matriz A tipo vetor e construir uma matriz B 
da mesma dimensão com os mesmos elementos de A acrescentados de mais 2. 
Colocar os elementos da matriz B em ordem crescente. 
Montar uma rotina de pesquisa, para pesquisar os elementos armazenados na matriz B.
'''
TAMANHO = 20

a =[]; b=[]

#Matriz A
for i in range(TAMANHO):
    a.append(int(input('Entre com um elemento: ')))

#matriz B com o valor do cubo de cada elemento de A
for i in range(TAMANHO):
    n = a[i] + 2
    b.append(n)

#ordenar elementos matriz B
for i in range(TAMANHO):
    for j in range(i):
        if b[i] < b[j]:
            aux = b[i]
            b[i] = b[j]
            b[j] = aux
print('Elementos de C ordenados')
print(b)

#busca o elemento no vetor B
busca = int(input('Entre com um numero a ser pesquisado: '))
for i in range(len(b)):
    if b[i] == busca:
        print('O elemento ', b[i], ' foi localizado na posição ', i)


