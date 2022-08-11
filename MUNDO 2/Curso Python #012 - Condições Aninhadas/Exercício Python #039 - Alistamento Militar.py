from datetime import date
atual = date.today().year
nascimento = int(input('Ano em que nasceu: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade-18} anos.'
          f'\nSeu alistamento foi em {nascimento+18}. ')
elif idade == 18:
    print('Você tem que se alistar imediatamente!')

else:
    print(f'falta {18-idade} anos para seu alistamento.'
          f'\nSerá chamado em {nascimento+18}.')
