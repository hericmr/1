print('-=-'*20)
print('Programa de aprovação de emprestimo bancário')
print('-=-'*20)
casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = float(input('Em quantos anos você irá pagar o preço da casa? '))
percento = salario * 0.30
parcela = casa / (anos * 12)
if percento > parcela:
    print(f'Pra pagar uma casa no valor de {casa} em {anos} anos a prestação será de {parcela}')
    print(f'O preço das parcelas será de {parcela:.2f} reais')
else:
    print(' Você não tem dinheiro suficiente pra comprar a casa. '.)

