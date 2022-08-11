maior = 0
menor = 0
lista = list()
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c ==0 or n > lista[-1]: #c ==0 é o primeiro valor da lista. #lista[-1] último elemento da lista.
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista): #indo da posição 0 até o último elemento da posição.
            if n <= lista[posição]: #verificando dentro de cada posição se o próximo número é menor ou igual a ele.
                lista.insert(posição,n) #se ele for menor ou igual vai inserir o valor numa posição especifica.
                print(f'Adicionado na posição {posição} da lista.')
                break
            posição += 1
print('=-='*30)
print(f'Os valores digitados em ordem foram {lista}')
