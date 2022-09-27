times = ('Palmeiras','Internacional','Fluminense',
'Flamengo', 'Corinthians','Athletico-PR',
'Atlético-MG', 'América-MG', 'Goiás',
'São Paulo', 'Botafogo', 'Santos', 'Bragantino',
'Fortaleza', 'Ceará', 'Coritiba', 'Avaí',
'Cuiabá', 'Atlético-GO', 'Juventude')
print('=-'*20)
print(f'    lista de times do brasileirão'.upper())
print('=-'*20)
print(f'Os 5 primeiros são {times[:5]}')
print('=-'*40)
print(f'Os quatro ultimos times são {times[-4:]}')
print('=-'*40)
print(f'''Os times em ordem alfabética são: 
{sorted(times)}''')
print('=-'*40)
print(f'O Santos está na {times.index("Santos") + 1 }ª posição.')