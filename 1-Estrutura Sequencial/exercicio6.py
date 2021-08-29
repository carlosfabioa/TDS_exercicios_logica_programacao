'''
Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula: 
PRESTRAÇÃO = VALOR + (VALOR * (TAXA / 100) * TEMPO)
'''

### ENTRADA ###
valor = float(input('Entre com o valor da prestação: '))
taxa = float(input('Entre com a taxa: '))
tempo = int(input('Entre com a quantidade de dias em atraso: '))

### PROCESSAMENTO ###
prestacao = valor + (valor * (taxa / 100) * tempo)

### SAÍDA ###
print('O valor da prestação atualizado é: ', prestacao)