from random import sample
lista = []
color = ('\033[m', '\033[1;97;42m','\033[32m' )
print(f'{color[1]} Gerador de Jogos Mega-Sena. {color[0]}\n'.center(25))
quant_jogos = int(input('Quantos jogos você quer? '.center(29)))
print(f'{color[2]}~{color[0]}'*40)
for numeros in range(1,61):
    lista.append(numeros)
for c in range(quant_jogos):
    jogo = sample(lista, 6)
    jogo.sort()
    print(f'{color[1]} Jogo {c+1}: {color[0]}',f' {color[2]}-{color[0]}'.join(str(f'{jogo:>3}')for jogo in jogo))
print(f'{color[2]}~{color[0]}'*40)
