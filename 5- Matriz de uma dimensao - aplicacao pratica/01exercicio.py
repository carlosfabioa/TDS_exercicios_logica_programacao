'''
a.	Ler 12 elementos de uma matriz tipo vetor, colocá-los em ordem decrescente 
e apresentar os elementos ordenados
'''

vetor = []
#entrada dos elementos do vetor
for i in range (12):
    vetor.append(int(input('Entre com um numero: ')))
#ordena o vetor
for i in range(12):
    for j in range (i):
        if vetor[i] > vetor[j]:
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux

print (vetor)