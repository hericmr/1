print('Olá forasteiro, esse programa fala quantas latas de tinta você precisará usar na sua parede.')
a=float(input('Qual é a altura da parede? '))
l=float(input('Qual é a largura dessa parede? '))
print(f'Sua parede tem {a*l} metros quadrados e voce precisará de {(a*l)*0.5:.2f} latas de tinta')