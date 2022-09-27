# cabeçalho
print('*' * 40)
print('           Caixa eletronico')
print('*' * 40)
#receber entrada do valor a ser retirado
valor = int(input('Quando você deseja sacar? '))
#fazer a divisão 50 reais 20 10 1
beijaflor = garça = macaco = arara= onças = 0
while valor >= 50:
    onças = valor // 50
    break
valor -= (onças * 50)
while valor >= 20:
    macaco = valor // 20
    break
valor -= macaco * 20
while valor >= 10:
    arara = valor // 10
    break
valor -= arara * 10
while valor >= 5:
    garça = valor // 5
    break
valor -= garça * 5
while valor >= 1:
    beijaflor = valor // 1
    break
valor -= beijaflor
print (f'''{onças} notas de 50 reais
{macaco} notas de vinte reais
{garça} notas de cinco reais
{beijaflor} notas de um real''')