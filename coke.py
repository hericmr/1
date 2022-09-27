moeda = int(input('Introduza a moeda: '))
refri = 50
troco = refri - moeda
while troco > 0:
    print(f'Amount due: {troco}')
else:
    print(f'Change owed: {-troco}')
