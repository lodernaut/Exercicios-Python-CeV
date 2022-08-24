ficha = {}
from random import randint
color = ('\033[m', '\033[1;97;42m','\033[32m' )
print(f'{color[1]}    Valores Sorteados.   {color[0]}\n'.center(63))

for c in range(4):
    dado = randint(1, 6)
    print(f"Jogador{c+1} tirou o dado {dado}.".center(49))
    ficha[f'Jogador{c+1}'] = dado
print(f'{color[2]}~{color[0]}'*50)

for i, j in enumerate(sorted(ficha, key=ficha.get, reverse=True)):
    print(f"  {color[2]}→{color[0]} {i+1}º Vencedor {j}. tirou o dado {ficha[j]}.".center(49))
print(f'{color[2]}~{color[0]}'*50)

