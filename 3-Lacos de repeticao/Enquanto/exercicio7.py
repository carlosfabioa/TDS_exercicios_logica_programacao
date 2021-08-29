'''
Apresentar as potências de 3 variando de 0 a 15. Deve ser considerado que qualquer número 
elevado a zero é 1, e elevado a 1 é ele próprio. Deverá ser apresentado, observando a seguinte
definição:
3 elevado a 0 = 1
3 elevado a  1 = 3
3 elevado a 2 = 9
...
3 elevado a 15 = 14348907
'''

contador = 0
resultado = 1
while contador < 15:
    resultado = 3 * resultado
    if contador == 0:
        print(1)
    print(resultado)
    contador +=1  
