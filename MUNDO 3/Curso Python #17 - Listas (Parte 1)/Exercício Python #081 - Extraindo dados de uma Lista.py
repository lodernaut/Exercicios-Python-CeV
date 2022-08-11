num = []
while True:
    num.append(int(input('Digite um valor: ')))
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if stop == 'N':
        break
num.sort(reverse=True)
print(f'Você digitou {len(num)} elementos.')
print('Os valores em ordem decrescente: ',", ".join(str(num) for num in num))
print('O valor 5 faz parte da lista.' if 5 in num else 'O valor 5 não faz parte da lista.')
