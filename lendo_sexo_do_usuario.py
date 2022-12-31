# Algoritmo para dizer se a pessoa é do sexo feminino ou masculino

# Criando variável de controle
p = 1

# implementando o laço
while p == 1:
    # mensagem alternativa p/ sair do programa
    print('Para sair do programa digite "S" ou:')
    # variavel para captar sexo do usuário
    sexo = str(input('Digite o seu sexo [F/M]: ')).upper()
    # condicao para sair do programa
    if sexo == 'S':
        # exibindo mensagem ao sair do programa
        print('Saindo do programa...\n')
        # instrucao para parar o programa
        break
    # condicao para identificar o se o usuario é do sexo feminino
    if (sexo == 'F'):
        # mostrando na tela o sexo do usuario
        print('Você é do sexo feminino\n')
    # condicao para identificar o se o usuario é do sexo feminino
    elif (sexo == 'M'):
        # mostrando na tela o sexo do usuario
        print('Você é do sexo masculino\n')
    # opçao caso o usuario digite algo diferente do sexo
    else:
        # mensagem de erro para, caso o usuario digite algo diferente de F, M ou S
        print('Você digitou a opção errada\n')
        # se for digitado algo diferente de F, M ou S o algoritmo retorna para o loop
        continue
