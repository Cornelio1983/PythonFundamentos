# Algoritmo para mostar na tela a categoria do atleta de acordo com a sua idade

# Critérios:
# idade menor que 09 anos: mirim
# idade entre 10 e 14 anos: infantil
# idade entre 15 e 19 anos: junior
# idade igual a 20 anos: senior
# idade acima de 20 anos: master

# mostrando as categorias dos atletas
print('De 0 a 9 anos: .....Categoria Mirim')
print('De 10 a 14 anos: ...Categoria Infantil')
print('De 15 a 19 anos: ...Categoria Junior')
print('20 anos: ...........Categoria Senior')
print('Acima de 20 anos: ..Categoria Master\n')

# variavel para captar o ano atual
anoAtual = int(input('Digite o ano atual: '))

# criando variaveis para captar dados
anoNascimento = int(input('Digite o ano de nascimento do atleta: '))

# calculando a idade do atleta
idade = anoAtual - anoNascimento

# implementando lógica conforme critérios
if (idade <= 9):
    print('Atleta está na categoria Mirim\n')
elif (10 <= idade <= 14):
    print('Atleta está na categoria Infantil\n')
elif (14 < idade <= 19):
    print('Atleta está na categoria Junior\n')
elif (idade == 20):
    print('Atleta está na categoria Senior\n')
else:
    print('Atleta está na categoria Master\n')
