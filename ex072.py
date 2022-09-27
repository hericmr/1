a = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
     'sete','oito', 'nove', 'dez','onze','doze','treze','quatorze',
     'quinze','dezesseis','dezessete', 'dezoito' ,'dezenove','vinte')
while True:
    while True:
        escolha = int(input('Por favor, escolha um número de 0 a 20: '))
        if 0 <= escolha <= 20:
            break
        else:
            print('Tente novamente. ', end='')

    print(f' Você escolheu {a[escolha]}', end= ' ')
    sair = input('Quer continuar?[c/n]').strip().lower()[0]
    if sair == 'n':
        break
    elif sair == 'c':
        print('')
