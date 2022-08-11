while True:
    print('_' * 41)
    n1 = int(input('Digite um número para ver sua tabuada? '))
    if n1 <= 0:
        break
    for n2 in range(1,11):
        print(f'{n1} x {n2} = {n1*n2}')
print('Programa Tabuada encerrado. Volte Sempre!')
print('_' * 41)