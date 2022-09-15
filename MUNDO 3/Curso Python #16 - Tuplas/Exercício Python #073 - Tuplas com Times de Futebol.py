times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo',
'Vasco','Chapecoense','Atlético','Botafogo','Atlético-PR','Bahia','São Paulo',
'Fluminense','Sport Recife','EC Vitória','Curitiba','Avaí','Ponte preta',
'Atlético-GO')
print('-'*50)
print(f'Listas de time do Brasileirão:')
print(times)
print('-'*50)
print('Os 5 primeiros colocados:')
print(times[:5])
print('-'*50)
print('Times em ordem alfabética:')
print(sorted(times))
print('-'*50)
print('Em qual posição está o time da Chapecoense:')
print(f"Chapecoense está na {times.index('Chapecoense')+1}º posição.")
