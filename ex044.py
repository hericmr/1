print ('Bem vindo ao programa de pagamento das Casas Bahia!')
valor = float(input('Qual foi o valor da compra? '))
esc = int(input("""Escolha sua forma de pagamento:
[1] Para pagar a vista com dinheiro ou cheque ganhando 10% de desconto
[2] Para pagar a vista no cartão ganhando 5% de desconto
[3] Para pagar em até 2 vezes no cartão (preço normal)
[4] Para pagar em 3 vezes no cartão (20% de juros)\n"""))

if esc == 1:
    print (f'Você pagará {valor * 0.90}')
elif esc == 2:
    print (f'Você pagará {valor * 0.95}')
elif esc == 3:
    print (f'Você pagará {valor}')
else:
    print (f'Você pagará {valor * 1.20}')

