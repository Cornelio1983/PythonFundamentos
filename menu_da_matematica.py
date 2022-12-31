# importando o pacote sleep da biblioteca time
from time import sleep
# criando variavel de controle do laço
n = 1
# variaveis para captacao dos numeros
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um numero inteiro: '))
# implementação do laço
while (n == 1):
    # imprimindo borda superior do menu
    print('-'*25)
    # imprimindo o menu da mantemática
    print('O que você deseja fazer?')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] Sair do programa')
    # imprimindo borda inferior do menu
    print('-'*25)
    # variavel para guardar opcao do menu digitada pelo usuario
    opcao = int(input('Digite uma opção: '))
    # implementação das condições conforme escolha do menu
    # condicao caso o usuario escolha a opcao 1
    if (opcao == 1):
        # variavel para guardar valor da soma dos numeros
        somar = (num1 + num2)
        # imprimindo o valor da soma dos numeros
        print('A soma de {} + {} é: {}\n'.format(num1, num2, somar))
        # instrucao da biblioteca tima que faz o programa aguardar 1 segundo antes de mostrar o passo seguinte
        sleep(1)
        # instrução para continuar no loop do programa
        continue
    # condicao caso o usuario escolha a opcao 2
    elif (opcao == 2):
        # variavel para guardar valor da multiplicao dos numeros
        multiplicar = (num1 * num2)
        print('A multiplicacap de {} x {} é: {}\n'.format(num1, num2, multiplicar))
        # instrucao da biblioteca tima que faz o programa aguardar 1 segundo antes de mostrar o passo seguinte
        sleep(1)
        # instrução para continuar no loop do programa
        continue
    # condicao caso o usuario escolha a opcao 3
    elif (opcao == 3):
        # condicao para analisar se um num1 é maior que o num2
        if (num1 > num2):
            # mensagem para dizer que o num1 é maior que num2
            print('O numero {} é maior que {}\n'.format(num1, num2))
        # condicao para analisar de os numeros digitado são iguais
        elif (num1 == num2):
            # mensagem para dizer que os numeros são iguais
            print('Não ha diferenca de valor entre {} e {}, ambos são iguais!'.format(num1, num2))
        else:
            # mensagem para dizer que o num2 é maior que num1
            print('O numero {} é maior que {}\n'.format(num2, num1))
            # instrucao da biblioteca tima que faz o programa aguardar 1 segundo antes de mostrar o passo seguinte
            sleep(1)
            # instrução para continuar no loop do programa
            continue
    # condicao para digitar novos numeros
    elif (opcao == 4):
        # variaveis para captacao dos numeros
        num1 = int(input('Digite um numero inteiro: '))
        num2 = int(input('Digite um numero inteiro: '))
        # instrucao da biblioteca tima que faz o programa aguardar 1 segundo antes de mostrar o passo seguinte
        sleep(1)
        # instrução para continuar no loop do programa
        continue
    elif (opcao == 5):
        print('Saindo do programa...')
        # instrucao da biblioteca tima que faz o programa aguardar 2 segundos antes de mostrar o passo seguinte
        sleep(2)
        print('Fim do programa!')
        # instrução para sair do loop do programa
        break
    else:
        print('Opção incorreta')
        # tornar a mostra as opções do menu
        opcao