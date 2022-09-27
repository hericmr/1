dat = int(input('Digite um ano'))
uni = dat // 1 % 10
dez = dat // 10 % 10
cen = dat // 100 % 10
mil = dat // 1000 % 10
print (f'A data que vc digitou foi {dat}')
print (f'O valor {uni} é unidade')
print (f'O valor {dez} é dezena')
print (f'O valor {cen} é centenha')
print (f'O valor {mil} é milhar')
