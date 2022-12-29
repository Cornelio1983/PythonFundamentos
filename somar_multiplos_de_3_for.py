# Algoritmo para somar multiplos de 03 entres 1 e 500

# implementando lógica

#criando variavel para somar numeros impares
somaImpar = 0;

for num in range(1, 500):
    if (num % 3 == 0):
        print(num)
        somaImpar += num
print('A soma do numeros multiplos de três é {}\n'.format(somaImpar))
