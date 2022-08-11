pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1 #para mostrar os 10 primeiros termos
while cont <= 10:
    print(f'{termo} ⇀ ',end='')
    termo += r
    cont += 1
print('FIM')
