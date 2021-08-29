'''
Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. 
Para verificar se o número é ímpar, efetuar dentro da malha a verificação lógica
desta condição com a instrução se, perguntando se o número é ímpar; sendo, mostre-o; 
não sendo, passe para o próximo passo.
'''
#iniciamos um contador para usar como critério de parada 
contador = 0

while contador <= 20:
    if contador %2 != 0:
        print(contador)
    # a cada laço acrescentamos mais um à variável contador.
    # quando a variavel contador atingir 20 o laço para
    contador += 1 

