total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1 or preco < menor:  # comando (or preco < menor:) simplificou o else abaixo
        menor = preco
        pMENORVALOR = produto
    #    else:
    #        if preco < menor:
    #            menor = preco
    #            pMENORVALOR = produto

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar: S/N? ')).strip().upper()
    if stop == 'N':
        break
print(f"{' FIM DO PROGRAMA. ':-^30}")
print(f'Total da compra foi: R${total:.2f}')
print(f'Temos {totmil} produto custando R$1.000,00 ou mais.')
print(f'O produto mais barato é o {pMENORVALOR} e seu valor: R${menor:.2f}')
