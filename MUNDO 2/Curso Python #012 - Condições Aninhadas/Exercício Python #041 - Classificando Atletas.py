from datetime import date
nascimento = int(input('Sua data de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade <= 9:
    print(f'Idade {idade} anos. Atleta Mirim.')
elif idade <= 14:
    print(f'Idade {idade} anos. Atleta Infantil.')
elif idade <= 19:
    print(f'idade {idade} anos. Atleta junior.')
elif idade <= 25:
    print(f'Idade {idade} anos. Atleta sênior.')
else:
    print(f'Idade {idade} anos. Atleta master.')