#Algoritmo para dizer se um número é maior ou menor

#variavel para captar numeros inteiros
primeiroNumero = int(input('Digite um numero inteiro: '))
segundoNumero = int(input('Digite outro numero inteiro: '))

#implementando lógica par dizer qual numero é maior, menor ou se sao iguais
if (primeiroNumero > segundoNumero):
    print('O primeiro valor é maior!\n')
elif (primeiroNumero < segundoNumero):
    print('O segundo valor é maior!\n')
else:
    print('O dois valores são iguais!\n')