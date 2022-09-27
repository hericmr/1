
velo=float(input('Qual foi a sua velocidade máxima? '))
if velo > 80:
    print('Você passou de 80km por isso foi multado!')
    multa = (velo - 80) * 7
    print(f'Você recebeu uma multa de {multa} reais')
else:
    print('Você esta dentro do limite de velocidade')
print('Tenha um bom dia')
