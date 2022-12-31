#PROGRAMA PARA CONTAR EXCLUIR MULTIPLOS DE 5

#Criando variável contadora
cont = 0

#implementado o laço
while (cont < 50):
    #incrementando a variavel contadora de um em um
    cont += 1
    #implementando a condicao para excluir multiplos de 5
    if (cont % 5 == 0):
        #pulando resultado
        continue
    else:
        print(cont)