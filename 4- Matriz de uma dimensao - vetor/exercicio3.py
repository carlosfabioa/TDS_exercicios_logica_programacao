'''
Ler uma matriz A do tipo vetor com 15 elementos. Construir uma matriz B de mesmo tipo, 
sendo que cada elemento da matriz B seja a fatorial do elemento correspondente da matriz A
'''
LINHAS = 2

def fatorial(n):
    fatorial = 1
    for contador in range(1,n+1):
        fatorial *= contador
    return fatorial

vetorA= []
vetorB=[]

for i in range(LINHAS):
    numero = int(input('Entre com um elemento: '))
    vetorA.append(numero)

for i in range(LINHAS):
    vetorB.append(fatorial(vetorA[i]))

for i in vetorB:
    print(i)