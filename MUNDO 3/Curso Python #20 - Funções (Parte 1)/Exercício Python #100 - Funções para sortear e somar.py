from random import randint
números = list()


def sorteia(lista):
    print("-"*57)
    for c in range(5):
        sorteado = randint(1, 10)
        lista.append(sorteado)
    print(f"Numeros sorteados para lista:", ', '.join(str(lista)for lista in lista))


def somaPar(lista): 
    par = 0
    for num in lista:
        if num % 2 == 0:
            par += num
    print(f"Soma de pares da lista: {par}")
    print("-"*57)

sorteia(números)
somaPar(números)
