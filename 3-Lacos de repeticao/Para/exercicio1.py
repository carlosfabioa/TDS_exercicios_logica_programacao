#Apresente todos os valores numéricos inteiros ímpares situados na faixa de 1000 a 1500


#a função range tem o seguinte formato: Start, Stop, Step
#no exercicio inicia-se com 1001, para no 1500 e tem passo de 2 em 2
#assim, é a solução mais fácil para mostrar números impares
for i in range(1001, 1500, 2):
    print(i)