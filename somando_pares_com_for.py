# Algoritmo para somar numeros pares e dizer quantos dos digitados é par

# Critérios:
# ao digitar um numero, dividir ele por 2
# se o resto da divisao for igual a zero, o numero é par
# se o numero for par, devo somá-lo e apresentar a soma de todos eles
# apresentar quantos numeros da sequencia digitada são pares

# crição de variáveis para contar e somar numeros pares
contador = 0
somaPar = 0

# gerando um salto de linha antes da execução do algoritmo
print('\n')

# laço para contar os numeros
for i in range(0, 6):
    # variavel para captação de numeros
    num = int(input('Digite um numero inteiro: '))
    # condição para descobrir se o numero é par ou não
    if (num % 2 == 0):
        # variavel para somar os numeros pares
        somaPar += num
        # variável para contar quais dos numeros é par
        contador += 1
# mostrando na tela a quantidade de numeros pares e o valor de sua soma
print('Você informou {} numeros pares e a soma deles é: {}\n'.format(contador, somaPar))
