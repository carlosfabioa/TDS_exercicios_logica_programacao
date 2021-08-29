#Apresentar os resultados de uma tabuada de um número qualquer

tabuada = int(input('Entre com a tabuada: '))
resultado = 1

for i in range(1, 11):
    resultado = tabuada * i
    #usei o método format() para formatar saída 
    #mais informações https://docs.python.org/pt-br/3/tutorial/inputoutput.html#the-string-format-method
    print("{} x {} = {}".format(tabuada, i, resultado))