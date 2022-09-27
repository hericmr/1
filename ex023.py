nome = (input('Escreva seu nome inteiro: '))
print(f'Beleza, seu nome com letras maiusculas é: {nome.upper()}')
print(f'Seu nome com letras minusculas é: {nome.lower()}')
tamanho = len(nome) - nome.count(' ')
print(f'Seu nome tem {tamanho} letras')
separado = nome.split()
print(f'Seu primeiro nome é {separado[0]} e tem {len(separado[0])} letras.')



