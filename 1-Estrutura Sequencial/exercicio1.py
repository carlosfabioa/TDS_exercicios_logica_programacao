'''
Ler quatro números e apresentar o resultado dois a dois da adição e multiplicação, 
baseando-se na utilização da propriedade distributiva.  Ou seja, se forem lidas as
variáveis A, B, C e D, deverão ser somente somadas e multiplicadas A com B, A com C e a com D. 
Depois B com C, B com D e por fim C com D
'''
### ENTRADAS ####
# A função input() é usada para ler a entrada do usuário.
# A função input() lê essa entrada como string
# A função int() vai converter a entrada em string para número inteiro
a = int(input('Entre com o primeiro número: '))
b = int(input('Entre com o segundo número: '))
c = int(input('Entre com o terceiro número: '))
d = int(input('Entre com o quarto número: '))

### PROCESSAMENTO ###
#Efetuando as somas
soma1 = a + b
soma2 = a + c
soma3 = a + d
soma4 = b + c
soma5 = b + d
soma6 = c + d
#efetuando as multiplicações
mult1 = a * b
mult2 = a * c
mult3 = a * d
mult4 = b * c
mult5 = b * d
mult6 = c * d

### SAÍDAS ###
print('### Soma dos números ###')
print('Soma de A + B: ', soma1)
print('Soma de A + C: ', soma2)
print('Soma de A + D: ', soma3)
print('Soma de B + C: ', soma4)
print('Soma de B + D: ', soma5)
print('Soma de C + D: ', soma6)

print('\n ###Multiplicação dos números ###')
print('Multiplicação de A + B: ', mult1)
print('Multiplicação de A + C: ', mult2)
print('Multiplicação de A + D: ', mult3)
print('Multiplicação de B + C: ', mult4)
print('Multiplicação de B + D: ', mult5)
print('Multiplicação de C + D: ', mult6)