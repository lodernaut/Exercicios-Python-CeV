somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1,5):
    print(f'=== {pessoa}º Pessoa. ==='.center(20))
    nome = str(input('nome: ')).strip().title()
    idade = int(input('Idade: '))
    gênero = str(input('Gênero: ')).strip()
    somaidade += idade
    if pessoa ==1 and gênero in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if gênero in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if gênero in 'fF' and idade ==20:
        totmulher20 += +1


médiaidade = somaidade / 4
print(f'Média idade do grupo é {médiaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com 20 anos.')
