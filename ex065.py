soma = media = contador = 0
escolha = 'S'
while escolha == 'S':
    n = float(input('Insira sua nota em uma matéria: '))
    escolha = input('Quer continuar [s],[n]? ').upper()[0]
    contador += 1
    soma += n
print(f'{soma / contador} ')