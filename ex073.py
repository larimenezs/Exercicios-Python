# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Os 5 primeiros colocados
# B) Os últimos 4 colocados
# C) Times em ordem alfabética
# D) Em que posição está o time da Chapecoense


times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 35)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 35)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 35)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=' * 35)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 35)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição.')