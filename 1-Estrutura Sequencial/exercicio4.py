'''
Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula:
VOLUME  3.14159 * R ** 2 * ALTURA
'''

### ENTRADA ###
r = float(input('Entre com o raio: '))
altura = float(input('Entre com a altura da lata: '))

### PROCESSAMENTO ###
volume = 3.14159 * r ** 2 * altura

### SAÍDA ###
print('O volume da lata de óleo é: ', volume)