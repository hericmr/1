numero = int(input('Digite 1 numero inteiro: '))
for counter in range (1, numero, 1):
    if numero % counter == 0:
        print('\033[33m', end= ' ')
    else:
        print('\033[31m', end=' ')
    print(f'{counter}', end=' ')
