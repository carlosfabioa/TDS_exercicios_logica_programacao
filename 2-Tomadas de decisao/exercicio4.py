'''
Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem 
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. 
Se o valor da média for menor que 7, solicitar a nota do exame, somar com a média e 
obter nova média. Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo 
que o aluno foi aprovado em exame. Se o aluno não foi aprovado, indicar uma mensagem 
informando esta condição. Apresentar junto com as mensagens o valor da média do aluno, 
para qualquer condição.
'''

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))
nota4 = float(input("Entre com a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print('O aluno foi aprovado com a media: ', media)
else:
    print('Aluno em exame.')
    notaexame = float(input('Entre com a nota do exame: '))
    novamedia = (media + notaexame) / 2
    if novamedia >= 5:
        print('Aluno aprovado em exame com média: ', novamedia)
    else:
        print('Aluno reprovado com média após exame de: ', novamedia)
