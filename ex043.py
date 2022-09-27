print('Calculo do IMC!!!!!!!!')
peso = float(input ('Digite seu peso: '))
alt = float(input('Digite sua altura'))
imc = peso / (alt ** 2)
print(f'Seu IMC é {imc}')
if imc <= 18.5:
    print('E você esta abaixo do peso ideal.')
elif 18.5 < imc < 25:
    print('E você está dentro do peso ideal')
elif 25 < imc < 30:
    print('E você está com sobrepeso')
elif 30 < imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
