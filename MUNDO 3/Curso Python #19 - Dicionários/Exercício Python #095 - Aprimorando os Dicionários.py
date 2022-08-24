dados_clear = {}
lista = []
while True:
    dados_clear['Nome'] = str(input("Nome do jogador: ")).strip().title()
    dados_clear['Partidas'] = int(input(f"Quantas partidas {dados_clear['Nome']} jogou? "))
    dados_clear['Gols'] = [int(input(f"  → Quantos gols na {c+1}º partida? ")) for c in range(dados_clear['Partidas'])]
    dados_clear['Total'] = sum(dados_clear['Gols'])
    lista.append(dados_clear.copy())
    dados_clear.clear()
    while True:
        stop = str(input("Quer adicionar um novo jogador? [S/N]: ")).strip().upper()[0]
        if stop in 'SN':
            break
        print("Por favor, Digite apenas 'S' para Sim ou 'N' para Não.")
    if stop in 'N':
        break
print("=-="*20)
print(f"{f'Cód.':<6}|{f'Nome.':<20}|{f'Gols.':<20}|{f'Total.':<6}")
print("-"*60)
for i, j in enumerate(lista):
    print(f"{i:<6}|{j['Nome']:<20}|{' - '.join(map(str, j['Gols'])):<20}|{str(j['Total']):<6}")
print("=-="*25)
while True:
    stats = int(input("  → Use o [Cód.] para mostrar dados do jogador ou digite [999] para sair: "))
    if stats == 999:
        print("Finalizado.")
        break
    if stats <= len(lista) -1:
        values = ' '.join(map(str, lista[stats].values()))
        keys = ' '.join(lista[stats])
        items = ' '.join(f'{key}: {value} |' for key, value in lista[stats].items())
        print(items)
        print("-"*74)
    else:
        print("Por favor, Digite apenas o Núm-Cód do jogador ou [999] para sair:")
