pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = pt + (10 - 1) * r #FÓRULA PARA CALCULAR O DÉCIMO TERMO.
for c in range(pt,décimo +  r, r):
    print(f'{c}', end=' ⇀ ')