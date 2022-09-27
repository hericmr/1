import random  #importa a biblioteca de aleatoriedade

lista = [] # seila
n = int(input('\nn: '))  #pede pra usuario colocar um nº e o \n serve pra pular uma linha
for i in range(n):  #cria uma repetição
    ichave = int((random.random() * 99) % 100)  #define parametros para a repetição: um numero inteiro aleatorio vezes 99, módulo de 100
    lista.append(ichave) #eita

print(lista)
