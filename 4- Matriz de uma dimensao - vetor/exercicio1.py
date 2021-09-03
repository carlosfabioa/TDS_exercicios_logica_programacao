#Ler 10 elementos de uma matriz tipo vetor

vetor=[] #declarando um vetor vazio

for i in range(1, 10):
    vetor.append(i) #adicionando elementos ao vetor. Função append adiciona no final da lista

for i in vetor:
    print(i)