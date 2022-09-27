from random import randint
print('Meu nome é HAL-9000, tudo bem?')
print('Olha, eu vou pensar num numero de 1 a 5')
pc = randint(1, 5) # faz o computador pensar
jogador = int(input('Blz, já pensei. Agora tenta adivinhar qual foi o numero: '))
print(f'Eu pensei no numero {pc} e vc pensou no numero: {jogador}...')
if jogador == pc:
    print('Parabéns, vc acertou')
else:
    print ('vc errou!!!')
print ('-----fim-----')


