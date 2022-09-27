print('\033[34m', end='')
print('-'* 24)
print(' SEQUÊNCIA DE FIBONACCI!')
print('-'* 24)
print('\033[35m', end='')
t1 = 0
t2 = 1
n = int(input('Quantos termos você quer?'))
contador = 3
print('\033[m', end='')
print(f'{t1} {t2}', end='')
while contador <= n:
    t3 = t1 + t2
    print (f' {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
