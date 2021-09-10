'''
Ler duas matrizes do tipo vetor A com 20 elementos e B com 30 elementos. 
Construir uma matriz C, sendo esta a junção das duas outras matrizes. 
Desta forma, C deverá ter a capacidade de armazenar 50 elementos.
'''

LINHAS_A = 20
LINHAS_B = 30

a =[]; b = []; c = []


#Vetor A
print('Vetor A')
for i in range(LINHAS_A):
    n = int(input('Entre com um número: '))
    a.append(n)

print('\nVetor B')

#Vetor B
for i in range(LINHAS_B):
    n = int(input('Entre com um número: '))
    b.append(n)

#Vetor C
for i in range(LINHAS_A):
    c.append(a[i])
    
for i in range(LINHAS_B):
    c.append(b[i])


print(c)
