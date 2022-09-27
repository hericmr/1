from time import sleep
print('------>SUPER GERADOR DE PA.<------')
print('=-'* 17)
numero = int(input('Dai me o primeiro termo de uma PA: '))
razao = int(input('Dai-me a razão desta PA: '))
termo = numero
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end='')
        sleep(0.1)
        print('...', end='')
        termo += razao
        cont += 1
        sleep(0.2)
    print('PAUSA')
    mais = int(input('Quantos termos mais vc quer?'))
print(f'Progressão terminada com {total} termos')