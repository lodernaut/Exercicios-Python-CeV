n = int(input('Digite seu número: '))
print(f'Calculando: {n}!')
c = n
f = 1 #fator nulo de multiplicação é 1
while c > 0:
    print(f'{c}',end=' ')
    print('x ' if c > 1 else '= ',end='')
    f *= c
    c -= 1
print(f'{f}')

