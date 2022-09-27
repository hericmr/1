sexo = str(input('Qual é o seu sexo (M ou F N para não quero falar) ? ')).upper().strip()[0]
while sexo not in 'MFN':
    print('Digite novamente')
if sexo == 'M':
    print('homi')
elif sexo == 'F':
    print('mulér')
else:
    print('não identificade')