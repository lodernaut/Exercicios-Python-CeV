valor = list()
for cont in range(0,5):
    valor.append(int(input(f'Digite um valor para posição {cont}: ')))
print('=-='*16)
print(f'Você digitou os valores: ',end='')
print(*valor,sep=', ')
print(f'O maior valor digitado foi: {max(valor)} nas posições ',end='')
for i, v, in enumerate(valor): #i igual índice #v igual valor.
    if v == max(valor):
        print(f'{i}... ',end='')
print(f'\nO menor valor digitado foi: {min(valor)} nas posição ',end='')
for i, v, in enumerate(valor):
    if v == min(valor):
        print(f'{i}... ',end='')
print('\nFIM')