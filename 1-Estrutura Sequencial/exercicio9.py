'''
Uma loja de animais precisa de um programa para calcular os custos de criação de coelhos. 
O custo é calculado com a fórmula CUSTO = (NR_COELHOS * 0.70) /18 + 10. O programa deve 
ler um valor para a variável NR_COELHOS e apresentar o valor da variável CUSTO
'''

### ENTRADA ###
nr_coelhos = int(input('Entre com o número de coelhos: '))

### PROCESSAMENTO ###
custo = (nr_coelhos * 70) / 18 + 10

### SAÍDA ###
print('O custo para criação de ', nr_coelhos, ' coelhos é de ', custo)