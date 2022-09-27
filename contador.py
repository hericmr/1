print('-'* 54)
print('             COEFICIENTE de RENDIMENTO')
print('-'* 54)
print('\033[35m', end='')
escolha = input('''Para saber a media de um numero conhecido de matérias 
digite [c] para ver a media de um numero desconhecido 
de matérias, digite [d], para sair, digite [s].''').strip().lower()[0]

if escolha == 'c':
    print('\033[34m', end='')
    print('Você quer a media de quantas matérias?')
    mat = int(input(''))
    soma = 0
    for heric in range (mat):
        n = float(input('Insira sua nota em uma das matérias: '))
        soma += n
    print('\033 (34m', end='')
    print(f' Seu coeficiente de rendimento é: {soma / mat}')
elif escolha == 'd':
    soma = media = contador = 0
    escolha = 's'
    while escolha == 's':
        print('\033[34m', end='')
        n = float(input('Insira sua nota em uma matéria: '))
        escolha = input('Quer continuar? [s], [n]? ').lower()[0]
        contador += 1
print('saindo...')