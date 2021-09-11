'''
b.	Ler 8 elementos em uma matriz A tipo vetor. Construir uma matriz B
 de mesma dimensão com os elementos da matriz multiplicados por 5. 
 Apresentar a matriz B na ordem crescente. Montar uma rotina para pesquisar
  os elementos armazenados na matriz B
'''
TAMANHO = 8

a = []
b = []
#entra com os elementos do vetor A
for i in range(TAMANHO):
    a.append(int(input('Entre com um elemento: ')))
#cria vetor B, (multiplicação de cada elemento do vetor A por cinco)
for i in range(TAMANHO):
    b.append(a[i]*5)
#ordena elementos do vetor B
for i in range(TAMANHO):
    for j in range(i):
        if b[i] < b[j]:
            aux = b[i]
            b[i] = b[j]
            b[j] = aux
#busca o elemento no vetor B
busca = int(input('Entre com um numero a ser pesquisado: '))
for i in range(len(b)):
    if b[i] == busca:
        print('O elemento ', b[i], ' foi localizado na posição ', i)
    
#print(b)