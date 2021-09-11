'''
d.	Ler uma matriz A com 12 elementos. Após a sua leitura, colocar
 os seus elementos em ordem crescente. Depois ler uma matriz B 
 também com 12 elementos. Colocar os elementos de B em ordem crescente.
 Construir uma matriz C, onde cada elemento de C é a soma do elemento 
 correspondente de A com B. Colocar em ordem crescente a matriz C e
  apresentar os seus valores
'''
TAMANHO = 12

a = []
b = []
c = []

#entrada elementos matriz A
print('ELEMENTOS DE A')
for i in range(TAMANHO):
    a.append(int(input('Entre com elementos de A: ')))

#ordenar elementos matriz A
for i in range(TAMANHO):
    for j in range(i):
        if a[i] < a[j]:
            aux = a[i]
            a[i] = a[j]
            a[j] = aux
print('Elementos de A ordenados')
print(a)

#entrada elementos matriz B
print('ELEMENTOS DE B: ')
for i in range(TAMANHO):
    b.append(int(input('Entre com os elementos de B: ')))

#ordenar elementos matriz B
for i in range(TAMANHO):
    for j in range(i):
        if b[i] < b[j]:
            aux = b[i]
            b[i] = b[j]
            b[j] = aux
print('Elementos de B ordenados')
print(b)

#cria matriz C (soma dos elementos de A com elementos de B)
for i in range(TAMANHO):
    c.append(a[i] + b[i])

print('Matriz c criada a partir da soma dos elementos: ', c)

#ordenar elementos matriz C
for i in range(TAMANHO):
    for j in range(i):
        if c[i] < c[j]:
            aux = c[i]
            c[i] = c[j]
            c[j] = aux
print('Elementos de C ordenados')
print(c)