t1, t2 = 0, 1
cont = 0
termos = int(input('Quantos temos você quer mostra? '))
if termos <= 0:
    print('Apenas números inteiros positivos.')
elif termos == 1:
    print(t1)
else:
    while cont < termos:
        print(f'{t1}', end='')
        print(' → ' if cont < termos-1 else '', end='')
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        cont += 1
