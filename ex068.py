from random import randint
while True:
    escolha = input('Par ou impar? [P/I]').strip().lower()[0]
    valor = int(input('Dê um valor: '))
    pc = randint(1, 5)
    if valor % 2 == 0:
        print(f'''O computador escolheu o valor {pc}, vc escolheu {valor}
a soma dos valores é {pc + valor}''')
        if pc + valor % 2 ==0:
            print('A soma dos numeroa é par! Você ganhou!')
        else:
            print('A soma dos numeros é impar! Você perdeu!')
            break
    else:
        print(f'''O computador escolheu o valor {pc}, vc escolheu {valor}
a soma dos valores é {pc + valor}''')
        if pc + valor % 2 != 0:
            print ('A soma dos valores é impar Você ganhou!')
        else:
            print('A soma dos valores é impar! Você perdeu')
            break