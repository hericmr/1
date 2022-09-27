from datetime import date
atual= date.today().year
print('PROGRAMA da CONFEDERAÇÃO NACIONAL de PESCA SUBMARINA')
ano = int ( input('Digite o ano do nascimento para saber qual é a sua categoria '))
idade = atual - ano
if idade < 9:
    print (f'Idade do atleta: {idade} anos. Categoria: Mexilhãozinho!')
elif idade < 14:
    print (f'Idade do atleta: {idade} anos, Categoria: Sargentinho!')
elif idade < 19:
    print (f'Idade do atleta: {idade} anos, Categoria Robalo!')
elif idade < 20:
    print (f'Idade do atleta {idade} anos. Categoria: Tubarão')
else:
    print (f'Idade do atleta: {idade} anos, Categoria: SHEREIA!')
