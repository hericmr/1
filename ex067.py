while True:
    print('-' * 57)
    print('          Quer ver a tabuada de qual valor?')
    print('-' * 57)
    tab = int(input())
    if tab < 0:
        break
    for c in range (1, 11):
        print(f'{tab} x {c} = {tab * c}')
print('acabou')
