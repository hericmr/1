from time import sleep
n1 = int(input('De um numero: '))
n2 = int(input('Fale outro numero'))
opção = 0
print("""    [ 1 ] soma
    [ 2 ] multiplicação
    [ 3 ] divisão
    [ 4 ] subtração
    [ 5 ] sair do programa""")
while opção !=5:
    opção = int(input('Qual é a sua opção?'))
    sleep(2)
    if opção == 1:
        print (f'{n1} + {n2} = {n1 + n2}')
    elif opção == 2:
        print (f'{n1} x {n2} = {n1 * n2}')
    elif opção == 3:
        print (f'{n1} - {n2} = {n1 / n2}')
    elif opção == 4:
        print(f'{n1} - {n2} = {n1 - n2}')
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida tente novamente:')
print('Fim do programa!')