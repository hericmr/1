from random import randint
from time import sleep
print('Meu nome é HAL-9000, tudo bem...?!')
print('Olha, vou pensar num numero de 1 a 10e vc tenta adivinhar...')
pc = randint(1, 10)
sleep(2)
acertou = False
while not acertou:
    jogador = int(input('Blz, qual é o seu palpite?'))
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('O numero é maior, tente de novo')
        else:
            print('O numero é menor, tente novamente')
print(f'Eu pensei no numero {pc} e vc pensou no numero: {jogador}...')
if jogador == pc:
    print('Parabéns, vc adivinhou')
