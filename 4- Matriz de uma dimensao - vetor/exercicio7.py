'''
Ler 15 elementos de uma matriz A do tipo vetor. Construir uma matriz B do mesmo tipo,
observando a seguinte lei de formação: “Todo elemento de B deverá ser o quadrado 
do elemento de A correspondente”
'''
LINHAS = 15

vetorA = []
vetorB = []

for i in range(LINHAS):
    n =int(input('Entre com o numero: '))
    vetorA.append(n)

for i in range(LINHAS):
    vetorB.append(vetorA[i] * vetorA[i])

print(vetorB)