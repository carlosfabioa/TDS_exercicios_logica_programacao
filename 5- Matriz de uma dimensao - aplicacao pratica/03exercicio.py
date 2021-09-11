'''
c.	Ler a matriz A do tipo vetor com 15 elementos. Construir uma matriz B de
mesmo tipo, sendo que cada elemento da matriz B seja a fatorial do elemento
correspondente da matriz A. Apresentar os elementos da matriz B ordenados de forma crescente
'''
TAMANHO = 15

a =[]
b =[]

#entra com elementos do vetor A
for i in range(TAMANHO):
    a.append(int(input('Entre com o elemento: ')))

#calcula fatorial e cria vetor B
for i in a:
    fatorial = 1
    for j in range(1,i +1):
        fatorial *= j
    b.append(fatorial)

#ordena vetor B
for i in range(TAMANHO):
    for j in range(i):
        if b[i] < b[j]:
            aux = b[i]
            b[i] = b[j]
            b[j] = aux

print(b)