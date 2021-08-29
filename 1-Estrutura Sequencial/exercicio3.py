'''
Ler a temperatura em graus Fahrenheit e apresentá-la convertida em graus Centígrados.
A fórmula de conversão é C  (F – 32) * (5 / 9), onde F é a temperatura em Fahrenheit
e C é a temperatura em Centrígrados.
'''
### ENTRADA ###
f = float(input('Entre com a temperatura em Fahrenheit: '))

### PROCESSAMENTO ###
c = (f-32) * (5 / 9)

### SAÍDA ###
print('A temperatura convertida para Centrigrados é: ', c)