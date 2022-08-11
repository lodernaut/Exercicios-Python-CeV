from random import randint
n = tuple(randint(1,9) for c in range(1,6))
print(f"Valores sorteados: {n} maior número: {max(n)} menor número: {min(n)}")
if n==n:
    print('Houve números repetidos')
else:
    print('Não houve números repetidos')