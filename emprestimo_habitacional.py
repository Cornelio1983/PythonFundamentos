#ALGORIMTO PARA DIZER SE UMA PESSOA PODE FINANCIAR OU NÃO UM CASA

#Variaveis
#captar a renda do usuario
#captar o valor da casa
#quantos anos será pago a casa

#Critérios:
#o valor da parcela não pode exceder a 30% da renda do usuario

#criando variaveis para capatar dados
salarioMensal = float(input('Digite o valor da sua renda: '))
valorImovel = float(input('Digite o valor do imovel: '))
prazoPagamento = float(input('Em quantos anos será pago o financiamento: '))

#saltando espaço
print('\n')

#transformando prazoPagamento em meses
tempoPagamento = prazoPagamento * 12

#variavel para calcular o valor da prestacao mensal
prestacaoMensal = valorImovel / tempoPagamento

#variavel p/ calcular 30% do salario
percentualPermitido = salarioMensal * 30/100

#mostrando na tela salario mensal do usuario
print('Salario mensal: R${:.2f}'.format(salarioMensal))

#mostrando na tela prazo de pagamento
print('Tempo de financiamento, {:.0f} anos'.format(prazoPagamento))

#mostrando na tela valor da prestação mensal
print('Valor prestação mensal: R${:.2f}'.format(prestacaoMensal))

#implementando lógica condicional para condecer ou não o emprestimo
if (prestacaoMensal > percentualPermitido):
    print('Emprestimo não poderá ser concedido!')
    print('O valor da prestação mensal R${:.2f} excede a 30% da sua renda!\n'.format(prestacaoMensal))
else:
    print('Emprestimo poderá ser concedido!\n')