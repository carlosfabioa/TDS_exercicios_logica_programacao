'''
Apresentar o total da soma obtido dos cem primeiros números inteiros (1+2+3+4....+98+99+100)
'''
soma = 0 #iniciamos o acumulador com valor 0
contador = 0 # iniciamos um contador com valor 0

while contador <= 100:
    soma += contador # equivale a dizer: soma = soma + contador
    contador += 1 # a cada laço o contador é incrementado em 1
print(soma)