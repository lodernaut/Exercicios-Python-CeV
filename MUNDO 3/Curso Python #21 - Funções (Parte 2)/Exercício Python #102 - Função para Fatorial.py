def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    print(f)


numero = int(input('Número para o cálculo fatorial: '))
show = input('Deseja resultado detalhado (Sim / Não): ').strip().upper()[0]
while show not in 'SN':
    show = input('Detalhar o cálculo: (Sim / Não): ').strip().upper()[0]
if show in 'S':
    show = True
    print("Detalhamento do cálculo: ", end='')
else:
    show = False
fatorial(numero, show)
