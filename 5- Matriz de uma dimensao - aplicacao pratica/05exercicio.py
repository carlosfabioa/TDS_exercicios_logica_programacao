'''
e.	Ler duas matrizes do tipo vetor A com 20 elementos e B com 30 elementos.
 Construir uma matriz C, sendo esta a junção das duas outras matrizes. 
 Desta forma, C deverá ter a capacidade de armazenar 50 elementos. 
 Apresentar os elementos da matriz C em ordem decrescente.
'''
TAMANHO_A = 20
TAMANHO_B = 30

a = []
b = []
c = []

#ler matriz A com 20 elementos
print('ELEMENTOS DA MATRIZ A')
for i in range(TAMANHO_A):
    n = int(input('Entre com elemento para matriz A: '))
    a.append(n)
    c.append(n) #elementos de A adicionados ao final da matriz C

#ler matriz B com 30 elementos
print('ELEMENTOS PARA A MATRIZ B')
for i in range(TAMANHO_B):
    n = int(input('Entre com elemento para matriz B: '))
    b.append(n)
    c.append(n) #elementos de B adicionados ao final da matriz C

#Apresentação da matriz C em ordem decrescente
for i in range(len(c)):
    for j in range(i):
        if c[i] > c[j]:
            aux = c[i]
            c[i] = c[j]
            c[j] = aux
print('Elementos de C ordenados em ordem decrescente')
print(c)