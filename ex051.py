numero = int(input('Dê o primeiro termo de uma PA: '))
razao = int(input('Dai-me a razão desta PA: '))
decimo = numero + (10 - 1) * razao
for heric in range (numero, decimo + razao, razao):
    print (f'{heric}', end='---')
print('ACABASTE')