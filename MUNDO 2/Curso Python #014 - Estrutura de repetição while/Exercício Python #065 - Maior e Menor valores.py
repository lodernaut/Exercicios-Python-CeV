stop = 's'
menor = maior = cont = soma = média = 0
while stop == 's':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    stop = str(input('Quer continuar S/N: ')).strip().lower()[0]
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

média = soma / cont
print(f'Você digitou {cont} números e a média foi {média:.2f} ')
print(f'O maior número foi {maior} e o menor número foi {menor}')
print('FIM')
