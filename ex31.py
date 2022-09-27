viagem = float(input('Quantos kms vc viajou? '))
if viagem < 200.0:
    preço = viagem * 0.50
    print(f'Vc tem que pagar R${preço:.2f}')
else:
    preço = viagem * 0.45
    print(f'Vc tem que pagar R${preço:.2f}')