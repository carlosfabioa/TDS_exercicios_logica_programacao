#Apresentar o fatorial de N números inteiros

n = int(input('Entre com um numero: '))
fatorial = 1

if n == 0:
    print(1)
else:
    for i in range(1,n + 1):
        fatorial *= i
    print(fatorial)