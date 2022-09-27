print("""Esse programa define se o valor de 3 medidas diferentes 
   podem formar um triangulo triangulo é isoceles, 
              equilatero ou escaleno""")
m1 = int(input('Informe o valor da medida de um lado do triangulo '))
m2 = int(input('Informe o valor da  medida de outro lado '))
m3 = int(input('Agora informe o valor da medida do ultimo lado do triangulo'))
final = str('Suas medidas não formam um triangulo :( ')
if m1 == 0 or m2 == 0 or m3 == 0:
    print(final)
elif m1 < m2 + m3 and m2 < m1 + m3  and m3 < m1 + m2:
    if m1 == m2 == m3:
        print('Suas medidas formam um triangulo equilatero!')
    elif m1 == m2 and m1 != m3 or m2 == m3 and m2 != m1 or m3 == m1 and m3 != m2:
        print('Suas medidas formam um triangulo isosceles!')
    else:
        print('Suas medidas formam um triangulo escaleno!')
else:
    print(final)
