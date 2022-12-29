#DIZENDO SE O PROGRAMA É PAR OU IMPAR

#implementando o laço
for numero in range(1, 11):
    #implementando condição para dizer se o numero é par ou impar
    if (numero % 2 == 0):
        #mensagem para dizer que o numero é par
        print('O numero {} é par'.format(numero))
    else:
        #mensagem para dizer que o numero é impar
        print('O numero {} é impar'.format(numero))