# Objetivos:
# mostar a media da idade dessas pessoas
# mostar o nome do homem mais velho
# mostrar quantas mulheres tem menos de 20 anos

# criando variaveis para guardar numeros e nome
homemMaisVelho = 0
homemMaisNovo = 0
nomeHomemMaisVelho = '0'
nomeHomemMaisNovo = '0'
homem = 0
mulher = 0
idade = 0
menosqueVinte = 0

# criando o laço
for i in range(1, 5):
    # enumerando a ordem de digitação das pessoas
    print('----- {}° PESSOA -----'.format(i))
    # criando variavel para captar nome da pessoa
    nomePessoa = input('Digite seu nome: ').capitalize()
    # criando variavel para captar a idade da pessoa
    idadePessoa = int(input('Digite sua idade: '))
    # criando variavel para captar o sexo da pessoa
    sexoPessoa = input(
        'Digite seu sexo - F (Feminino) - M (Masculino): ').upper()
    # incrementando o laço de um em um
    i += 1
    # implementando condição para contar homenes e mulheres
    if (sexoPessoa == 'F'):
        # variavel para contar numero de mulheres
        mulher += 1
    else:
        # variavel para contar numero de homens
        homem += 1
    # implementando condicao para mostrar mulher com idade menor que 20
    if (idadePessoa < 20 and sexoPessoa == 'F'):
        # variavel para contar numero de mulheres abaixo de 20 anos
        menosqueVinte += 1
    # implementando condicao para mostrar nome e idade do homem mais velho e mais novo
    if (sexoPessoa == 'M'):
        # implementando condicao para descobrir homem mais velho
        if (idadePessoa > homemMaisVelho):
            # variavel para guardar a idade do homem mais velho
            homemMaisVelho = idadePessoa
            # variavel para guardar nome do homem mais velho
            nomeHomemMaisVelho = nomePessoa
        elif (idadePessoa < homemMaisNovo):
            # variavel para guardar idade do homem mais novo
            homemMaisNovo = idadePessoa
            # variavel para guardar nome do homem mais novo
            nomeHomemMaisNovo = nomePessoa
    # criando variavel para calcular a media das idades
    mediaIdade = (idadePessoa)/4
    # saltando um linha
    print('\n')
# mostrando a média das idades na tela
print('A média das idades é: {} anos'.format(mediaIdade))
if (mulher == 0):
    print('Não foi cadastrado nenhuma pessoa do sexo feminino!')
else:
    # mostrando quantas pessoas são mulheres
    print('Quantos são mulheres? {}'.format(mulher))
    # mostrando quantas mulheres tem menos de 20 anos
    print('Quantas mulheres tem menos que 20 anos? {}'.format(menosqueVinte))
    # mostrando quantas pessoas são homens
if (homem == 0):
    print('Não foi cadastrado nenhuma pessoa do sexo masculino!')
else:
    print('Quantos são homens? {}'.format(homem))
    # mostrando o nome do homem mais velho e sua respecitiva idade
    print('{} é o homem mais velho com {} anos de idade'.format(
        nomeHomemMaisVelho, homemMaisVelho))
    # mostrando o nome do homem mais novo e sua respectiva idade
    print('Ao passo que {} é o homem mais novo com {} anos de idade\n'.format(
        nomeHomemMaisNovo, homemMaisNovo))