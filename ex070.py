caro = soma = contador = menor=  0
barato = ' '
# cabeçalho
print('*' * 40)
print('                Lojinha')
print('*' * 40)
# laço infinito que pede produto, preço e pergunta se usuario quer continuar ou terminar
while True:
    produto = input('Nome do produto: ')
    valor = float(input('Preço em R$:'))
    contador += 1
# algoritimo para registrar o produto mais barato
    if contador == 1 or valor < menor:
        menor = valor
        barato = produto
# vai somando o preço dos produtos a cada loop
    soma += valor
# computa o os produtos que custaram mais de 100 reais
    if valor >= 100:
        caro += 1
# pergunta se deseja continuar ou deseja sair
    finit = ' '
    while finit not in 'cs':
        finit = input('Continuar ou sair? [c/s]: ').strip().lower()[0]
    if finit == 's':
        break
# fim do programa com total da compra , produto que custou mais de R$ 100.00, produto mais barato
print(f'''Fim do programa
Voce gastou {soma:.2f} reais na lojinha
Você comprou {caro} produtos custando mais de R$ 1000.00
O produto mais barato que você comprou foi {barato} que custou {menor:.2f} reais''')
