soma = 0
for heric in range (1, 501, 2):
    if heric % 3 == 0:
        print(heric, end=' ')
        soma = soma + heric
print('\n A soma dos nºs impares e multiplos de 3 é ', soma)
