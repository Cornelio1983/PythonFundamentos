# importando pacote randint da biblioteca randon
from random import randint

# variavel para controle do laço
n = 1
# variavel para somar numeros de tentativas
tentativas = 0

# implementando o laço
while (n == 1):
    # variavel para guardar numero gerado pelo computador
    computador = randint(0, 10)
    # imprimindo borda no programa
    print('=' * 40)
    # mensagem do computador para o usuario
    print('Vou pensar em um numero entre 0 e 10, tente advinhar!')
    # imprimindo borda no programa
    print('=' * 40)
    # guardando numero de tentativas na variavel "tentativas"
    tentativas += n
    # solicitando ao usuario que digite um numero
    jogador = int(input('Em que numero pensei? '))
    # implementando condicao para saber se o usuario acertou ou nao
    if (jogador == computador):
        # caso o usuario acerte o numero do computador, mostrar essa mensagem
        print('Após {} tentativas você acertou, parabéns!'.format(tentativas))
        # se o usuario acertar o numero, parar de executar o programa
        break
    else:
        # se o usuário errar o numero, mostrar essa mensagem
        print('Numero errado, tente outra vez!')
        # instrução para continuar no loop
        continue
