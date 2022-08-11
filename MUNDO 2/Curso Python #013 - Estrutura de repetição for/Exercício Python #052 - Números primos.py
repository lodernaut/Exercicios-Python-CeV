soma = 0
num = int(input('Digite um número? '))
for c in range(1, num +1):
    if num % c ==0:
        soma += +1
        print('\033[34m', end=' ')
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')
print(f'\033[m\nO número \033[32m{num}\033[m foi divisível \033[34m{soma}\033[m vezes.')
if soma ==2:
    print('E por isso ele È PRIMO!')
else:
    print('E por isso ele NÂO È PRIMO!')