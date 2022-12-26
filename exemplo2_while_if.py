# PROGRAMA PARA IMPRIMIR MULTIPLOS DE 05 NUMA SEQUENCIA DE 50 NUMEROS

# Criando variável contadora
cont = 0

# implementado o laço
while (cont < 50):
    # incrementando a variavel contadora de um em um
    cont += 1
    # implementando condicao para excluir nao multiplos de 5
    if (cont % 5 == 0):
        # imprimindo valor da variavel na tela
        print(cont)
    else:
        # deixando de mostar nao multiplos de 5 numa sequencia de 50 numeros
        continue
