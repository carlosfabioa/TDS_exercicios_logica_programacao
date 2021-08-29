'''
Ler dois valores inteiros (variáveis A e B) e efetuar as operações de adição, 
subtração, multiplicação e divisão de A por B, apresentando ao final os quatro
resultados obtidos
'''

### ENTRADA ###
a = int(input('Entre com o primeiro número: '))
b = int(input('Entre com o segundo número: '))

### PROCESSAMENTO ###
adicao = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b # não estamos validando a divisão quando B for 0 (impossível dividir)

### SAÍDA ###
print('A adicionado a B = ', adicao)
print('B subtraido de A = ', subtracao)
print('A multiplicado por B = ', multiplicacao)
print('A divisão de A por B = ', divisao)