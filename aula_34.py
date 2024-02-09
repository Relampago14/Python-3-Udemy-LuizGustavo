# aula de introdução aos condicionais

acao = input('Você quer entrar ou sair? ')

if acao.lower() == 'entrar':
    print('Você entrou')

elif acao.lower() == 'sair':
    print('Você saiu')

else:
    print('Ação não interpretada.')
