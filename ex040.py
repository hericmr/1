n1 = float (input ('Qual foi a nota da P1? '))
n2 = float (input ('Qual foi a nota da P2? '))
m = (n1 + n2) / 2
if m == 6 or m > 6:
    print(f'Sua média é {m}! :D Tu passou!')
elif m < 4:
    print(f'Sua media é {m}!!! :[ Ta reprovado')
else:
    print(f'Eita, sua media foi {m} :/ Ta de repuperação')
