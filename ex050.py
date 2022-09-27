soma = 0
acumulador = 0
print('PROGRAMA QUE MOSTRA A SOMA DOS NUMEROS PARES DE 6 ENTRADAS')
for n in range(1,7):
    n = int(input(f'Digite o {n}o numero: '))
    if (n % 2) == 0:
        soma = soma + n
print(f'A soma dos 6 numeros pares que vc digitou é',soma)