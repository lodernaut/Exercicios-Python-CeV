maior = menor = 0
dados = list()
lista = list()
while True:
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if stop == 'N':
        break
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso é {maior} de ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}. ',end='')
print(f'\nO menor peso é {menor} de ',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}. ',end='')
 
