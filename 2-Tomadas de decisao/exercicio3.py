'''
ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem 
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. 
Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. 
Apresentar junto com uma das mensagens o valor da média do aluno para qualquer condição
'''
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))
nota4 = float(input("Entre com a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 5:
    print('Aluno aprovado com média:  ', media)
else:
    print('Aluno não aprovado, sua média foi de ', media)

