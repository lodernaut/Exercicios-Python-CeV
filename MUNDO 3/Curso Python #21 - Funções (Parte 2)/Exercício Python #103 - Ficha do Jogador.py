def ficha(footballPlayer='', goal=''):
    if footballPlayer in '':
        footballPlayer = 'Desconhecido'
    if not goal.isnumeric():
        goal = 0
    print(f"Jogador: {footballPlayer} \nGol(s): {goal}")


nome = input('Nome do Jogador: ').strip().title()
gol = input('Quantidade de gols: ').strip()
ficha(nome, gol)
