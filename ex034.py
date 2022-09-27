salario = float(input('Qual é o valor do salário? '))
if salario > 1250:
    novo = salario * 1.10
else:
    novo = salario * 1.15
print(f'Seu novo salário é de {novo}')
