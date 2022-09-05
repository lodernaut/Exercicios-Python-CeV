dados = {}
dados['Nome'] = str(input('Nome do Jogador: ')).strip().title()
dados['Partidas'] = int(input('Quantas partidas: '))
gols = [int(input(f'Quantos Gols na {c+1}º Partida: '))
        for c in range(dados['Partidas'])]
dados['Gols'] = gols
dados['Total'] = sum(gols)
print('=-='*21)
print(dados)
print('~'*63)
for k, v, in dados.items():
    print(f"O campo {k} tem o valor {v}")
print('~'*63)
print(f"O jogador {dados['Nome']} jogou {dados['Partidas']} partidas.")
for i, g in enumerate(dados['Gols']):
    print(f"  → Na {i+1}º partida, Fez {g} gols.")
print(f"Foi um total de {dados['Total']} gols.")
print(dados) 

