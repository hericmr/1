from time import sleep
contador = 1
while contador < 9999:
    print (contador, '...', end='')
    contador += 1
    sleep(0.05)
print ('acabou')