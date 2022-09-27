c=float(input("Informe a temperatura em ºC: "))
f=c * 1.8 + 32
print(f'A temperatura em {c} em fareheint é {f}')
if c <= 10:
    print('Realmente está um frio da porra!')
else:
    print('Uma temperatura agradável')