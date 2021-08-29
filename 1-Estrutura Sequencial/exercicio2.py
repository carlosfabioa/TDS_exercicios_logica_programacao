'''
Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem,
utilizando-se um automóvel que faz 12km por litro. Para obter o cálculo, o 
usuário deverá fornecer o tempo gasto na viagem e a velocidade média durante
a mesma. Desta forma, será possível obter a distância percorrida com a
fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta
calcular a quantidade de litros de combustível utilizada na viagem com a fórmula:
LITROS_USADOS = DISTÂNCIA / 12. O programa deverá apresentar os valores da 
velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de 
litros utilizada na viagem
'''

### ENTRADA ###
velocidade = float(input('Entre com a velocidade: '))
tempo = float(input('Entre com o tempo gasto: '))

### PROCESSAMENTO ###
distancia = tempo * velocidade
litros_usados = distancia / 12

### SAÍDA ###
print('O tempo gasto na viagem foi de ', tempo, 'horas')
print('A distância percorrida foi de ', distancia, 'kilometros')
print('A quantidade de litros de combustível utilizado foi de ', litros_usados, 'litros')