#Algoritmo para descobrir se é tempo do usuario se alistar ou não

#Critérios:
#se o usuário tiver menos que 18 anos, mostrar quanto tempo falta
#se o usuário tiver 18 anos dizer que está na hora de se alistar
#se o usuário tiver entre 19 e 45 anos, dizer que ele já passou na hora
#se o usuário tiver acima de 45 anos, dizer que o alistamento não é mais necessário

#criando variaveis para captar ano de nascimento e ano atual
anoAtual = int(input('Em que ano estamos? '))
anoNascimento = int(input('Qual o ano do seu nascimento? '))

#criando variavel para calcular a idade do usuario
idade = anoAtual - anoNascimento

#criando variavel para calcular quanto tempo falta para o usuario se alistar
diferencaAlistamento = 18 - idade

#implementando logica condicional para saber se está na hora do usuario de alistar
if (idade == 18):
  print(
    'Sua idade é {}, esse é o momento certo de você se alistar!'.format(idade))
elif (idade < 18):
  print(
    'Ainda falta {} ano(s) para você se alistar!'.format(diferencaAlistamento))
elif (18 < idade <= 45):
  print('Você têm {} anos, já passou da epóca de se alistar!'.format(idade))
else:
  print('Você não precisa se alistar mais!')