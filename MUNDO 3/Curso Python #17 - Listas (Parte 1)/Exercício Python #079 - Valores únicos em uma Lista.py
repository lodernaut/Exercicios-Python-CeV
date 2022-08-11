valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso ...')
    else:
        print('Valor duplicado! não será adicionado.')
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if stop == 'N':
        break
print('=-='*20)
print('Você digitou os valores: ',end='')
print(*sorted(valores),sep=', ')


print('finalizado.')
