'''
Ler duas matrizes A e B do tipo vetor com 20 elementos. Construir uma matriz C,
 onde cada elemento de C é a subtração do elemento correspondente de A com B
'''
LINHAS = 20
a =[]; b = []; c = []


#Vetor A
print('Vetor A')
for i in range(LINHAS):
    n = int(input('Entre com um número: '))
    a.append(n)

print('\nVetor B')
#Vetor B
for i in range(LINHAS):
    n = int(input('Entre com um número: '))
    b.append(n)

#Vetor C
for i in range(LINHAS):
    c.append(a[i] - b[i])

print('\nVetor C')
print(c)
