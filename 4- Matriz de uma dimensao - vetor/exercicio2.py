'''
Ler 8 elementos em uma matriz A tipo vetor. Construir uma matriz B de mesma dimensão com 
os elementos da matriz A multiplicados por 3. Apresentar a matriz B. O elemento B[1] 
deverá ser implicado pelo elemento A[1] * 3, o elemento B[2] implicado pelo emento A[2] * 3 
e assim por diante, até o 8
'''
vetorA = []
vetorB = []

for i in range(8):
    numero = int(input('Entre com um elemento: '))
    vetorA.append(numero)

for i in vetorA:
    vetorB.append(i*3)
    
for i in vetorB:
    print(i)