#captando nome do usuario
nome = str(input('Digite seu nome: '))
#usando IF para retornar mensagem ao usuario
if (nome == 'Gustavo'):
    print('Seu nome é bem feio!')
elif (nome == 'Pedro' or nome =="Maria" or nome == 'Paulo'):
    print('Seu nome é bem comum no Brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))