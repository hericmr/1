print ('E ai seu burro, \n bem vindo ao programa que revela se 3 medidas podem formar um triangulo')

m1 = float(input('Insira a medida de um dos lados do triangulo: '))
m2 = float(input('Insira mais um lado do triangulo: '))
m3 = float(input('Insira agora a medida do ultimo lado do triangulo: '))
if m1 < m2 + m3 and m3 < m2 + m1 and m2 < m3 + m1:
    print('Parabens, suas medidas podem formar um triangulo!')
else:
    print('Que peninha, vc não conseguiu formar triangulo com essas medidas!')

