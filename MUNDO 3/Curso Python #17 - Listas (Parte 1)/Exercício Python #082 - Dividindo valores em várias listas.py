numeros = list()
impares = list()
pares = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2==0 and n != 0:
       pares.append(n)
    elif n % 2 == 1 and n != 0:
        impares.append(n)
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if stop == 'N':
        break
print(f'A lista completa é: {numeros} ')
print(f'Lista de Pares: {sorted(pares)}')
print(f'Lista de Ímpares: {sorted(impares)}')



