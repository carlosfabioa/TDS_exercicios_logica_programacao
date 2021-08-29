'''
Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo. 
A série de Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34...etc. 
Esta série se caracteriza pela soma de um termo posterior com o seu anterior subsequente
'''
anterior = 0
seguinte = 1

for i in range(15):
    anterior, seguinte = seguinte, anterior + seguinte
    print(anterior)