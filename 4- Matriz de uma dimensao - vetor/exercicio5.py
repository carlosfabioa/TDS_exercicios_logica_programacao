'''
Ler duas matrizes A e B do tipo vetor com 15 elementos cada. 
Construir uma matriz C, sendo esta a junção da duas outras matrizes. 
Desta forma, C deverá ter o dobro de elementos, ou seja, 30.
'''

LINHAS = 15
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
    c.append(a[i])
    c.append(b[i])


print(c)
