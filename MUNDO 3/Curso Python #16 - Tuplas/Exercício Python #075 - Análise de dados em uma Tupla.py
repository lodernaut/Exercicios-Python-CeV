par = 0
numeros = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)}')
if 3 in numeros:
    print(f'O Valor 3 apareceu na {numeros.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado.')
contpar = 0
for p in numeros:
    if p %2==0:
        contpar += 1
if contpar ==0:
    print('Não foram digitados números pares.')
else:
    print('Os numeros pares são: ',end='')
    for p in numeros:
        if p % 2==0:
            print(f'{p} ',end='')
