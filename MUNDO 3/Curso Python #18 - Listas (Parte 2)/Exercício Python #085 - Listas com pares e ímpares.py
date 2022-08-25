lista = [[],[]]
for c in range(8):
    dados = int(input(f'Digite o {c+1}º valor: '))
    if dados % 2 ==0:
        lista[0].append(dados)
    else:
        lista[1].append(dados)
print(f'Valores digitados:', *lista[0]+lista[1],sep='  ')
lista[0].sort(),lista[1].sort()
print('Os valores pares digitados foram:',', '.join(str(lista[0])for lista[0] in lista[0]))
print('Os valores ímpares digitados foram:',', '.join(str(lista[1])for lista[1] in lista[1]))
