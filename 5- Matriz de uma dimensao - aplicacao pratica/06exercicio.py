'''
f.	Ler 30 elementos de uma matriz A do tipo vetor. Construir uma matriz B
de mesmo tipo, observando a seguinte lei de formação: Todo elemento de B 
deverá ser o cubo do elemento de A correspondente. Montar uma rotina de 
pesquisa, para pesquisar os elementos armazenados na matriz B
'''
TAMANHO = 30

a =[] ; b = []

for i in range(TAMANHO):
    a.append(int(input('Entre com um elemento: ')))

#matriz B com o valor do cubo de cada elemento de A
for i in range(TAMANHO):
    n = a[i] * a[i] * a[i]
    b.append(n)

#busca o elemento no vetor B
busca = int(input('Entre com um numero a ser pesquisado: '))
for i in range(len(b)):
    if b[i] == busca:
        print('O elemento ', b[i], ' foi localizado na posição ', i)



