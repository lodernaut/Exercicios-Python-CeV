maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}º pessoa: '))
    if pessoa ==1:                     #lendo o primeiro peso digitado
        maior= peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}KG e o menor peso foi {menor}KG.')