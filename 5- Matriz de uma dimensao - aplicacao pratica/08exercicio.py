'''
a.	Ler 12 elementos de uma matriz tipo vetor, colocá-los em ordem decrescente 
e apresentar os elementos ordenados
'''
TAMANHO = 12
vetor = []

for i in range(TAMANHO):
    elemento = int(input('Entre com o {}º elemento: '.format(i+1))) #usando a função format
    vetor.append(elemento)
    for j in range(i): #ordena os elementos em ordem decrescente
        if vetor[i] >= vetor[j]: 
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux

print(vetor)
