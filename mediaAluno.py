#Algoritmo para calcular Media do aluno e verificar se ele foi aprovado ou não

#Critérios:
#se a media for menor que 5.0: aluno reprovado
#se a media estiver entre 5.0 e 6.9: aluno em recuperação
#se media for maior ou igual a 7.0: aluno aprovado

#criando variaveis para captar notas
primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))

#criando variavel para calcular média do aluno
mediaAluno = (primeiraNota + segundaNota)/2

#saltando um linha
print('\n')
#imprimindo na tela valores das notas e médias
print('Sua primeira nota foi: {:.2f}'.format(primeiraNota))
print('Sua segunda nota foi: {:.2f}'.format(segundaNota))
print('Sua média é: {:.2f}\n'.format(mediaAluno))

#implementação das condições
if (mediaAluno < 5):
    print('Aluno reprovado!\n')
elif (5 < mediaAluno < 6.9):
    print('Aluno de recuperação!\n')
else:
    print('Aluno aprovado!\n')
