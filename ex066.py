contador = soma = 0
while True:
    valor = int(input('Digite um valor para somar (999 para parar) '))
    soma += valor
    contador += 1
    if valor == 999:
        break
print(f'A soma dos {contador} valores é {soma}')
