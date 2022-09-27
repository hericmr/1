val1 = int(input('Coloque um valor inteiro: '))
val2 = int(input('Coloque outro valor inteiro: '))
val3 = int(input('Coloque mais um valor inteiro: '))
if val1 < val2 and val1 < val3:
    print(f'o menor valor é {val1}')
if val2 < val1 and val2 < val3:
    print(f'o menor valor é {val2}')
if val3 < val1 and val3 < val2:
    print(f'O menor valor é {val3}')
if val1 > val2 and val1 > val3:
    print(f'o maior valor é {val1}')
if val2 > val1 and val2 > val3:
    print(f'o maior valor é {val2}')
if val3 > val1 and val3 > val2:
    print(f'o maior valor é {val3}')
