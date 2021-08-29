'''
Apresentar todos os números divisíveis por 4 que sejam menores que 200.
Para verificar se o número é divisível por 4, efetuar dentro da malha a 
verificação lógica desta condição com a instrução se, perguntando se o número é divisível; 
sendo, mostre-o; não sendo, passe para o próximo passo. A variável que controlará o contador 
deverá ser iniciada com valor 1
'''

contador = 1

while contador < 200:
    if contador %4 == 0:
        print(contador)
    contador += 1