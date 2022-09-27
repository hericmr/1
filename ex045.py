from random import randint
pc = randint(1,3)
print( '- CHOSE YOUR WEAPON '*40)
print("""JÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓÓ 
                            KEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEN')
                                                             POOOOOOOOOOOOOOOOOOOOOOOO !!!""")
humano = int(input("""[1] pedrita
[2] papelito
[3] tijierita"""))
if pc == 1:
    if humano == 1:
        print('VocÊ escolheu Rock e o computador tbm... Empate')
    elif humano == 2:
        print('Você escolheu papel e o computador pedra.... YOU WIN!')
    elif humano == 3:
        print('Você escolheu tesoura e o computador pedro.... Computador Wins')
elif pc == 2:
    if humano == 1:
        print('Você escolheu pedra e o computador papel.... Computador WINS!')
    elif humano == 2:
        print('Você escolheu papel e o PC tbm... EMPATE!!!!')
    elif humano == 3:
        print == ('Você escolheu tesoura e o computador escolheu papel..... VC VENCEU!!!')
elif pc == 3:
    if humano == 1:
        print('Você escolheu pedra e o computador escolheu tesoura..... You win')
    elif humano == 2:
        print('VocÊ escolheu papel e o pc escolheu tesoura... Computer wins')
    elif humano ==3:
        print('Você escolheu tesoura e o computador tbm..... empate')
else:
    print('Escolha um numero de 1 a 3!')