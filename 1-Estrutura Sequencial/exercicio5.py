'''
Ler dois valores para as variáveis A e B, efetuar a troca dos valores de
forma que a variável A passe a possuir o valor da variável B e que a variável B
passe a possuir o valor da variável A. Apresentar os valores trocados
'''

### ENTRADA ###
a = input('Entre com o primeiro número: ')
b = input('Entre com o segundo número: ')

### PROCESSAMENTO ###
temporario = a
a = b
b = temporario

### SAÍDA ###
print('Valores trocados: ', a, ' - ', b)