n = int (input('Fale um numero inteiro'))
opcao = int (input ("""Bele, agora digite 1 se quiser converter esse número para binário;
Ou digite 2 para converter esse seu numero em octagonal;
Ou digite 3 para converter seu numero para hexadecimal 
Ou digite 4 para elevar seu numero por 999999"""))
if opcao == 1:
    print (f'seu numero convertido para base binária é: {bin(n)}')
elif opcao == 2:
    print (f'Seu número na base octal seria: {oct(n)}')
elif opcao == 3:
    print (f'Seu numero na base hexadecimal seria: {hex(n)}')
elif opcao ==4:
    print (f'Seu numero elevado a 999999 é {(n ** 999999)}')
else:
    print('Opção inválida.... :(  ')
