'''
Ler 20 elementos de uma matriz A tipo vetor e construir uma matriz B de mesma 
dimensão com os mesmos elementos de A, sendo que estes deverão estar invertidos,
ou seja, o primeiro elemento de A passa a ser o último elemento de B, o segundo 
elemento de A passa a ser o penúltimo de B e assim por diante.
'''

LINHAS = 5

vetorA = []
vetorB = []

for i in range(LINHAS):
    n =int(input('Entre com o numero: '))
    vetorA.append(n)

for i in range(LINHAS -1, -1, -1):
    vetorB.append(vetorA[i])

print(vetorB)