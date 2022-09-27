contador = n = soma = 0
n = int(input("""Digite um numero para somar! [ 999 para parar ]"""))
while n != 999:
    soma += n
    contador += 1
    n = int(input("""Digite um numero para somar! [ 999 para parar ]"""))
print (f'Você digitou {contador} números e a soma foi {soma}')



