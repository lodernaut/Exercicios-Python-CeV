lista = [[0,0,0,],[0,0,0,],[0,0,0,]]
somapares = maiorsegcoluna = somatercoluna = 0
for l in range(3):
        for c in range(3):
                lista[l][c]=int(input(f'[ Matriz {l} ] {c}º valor: '))
print('=-=' * 15)
for l in range(3):
        for c in range(3):
                print(f'[{lista[l][c]:^5}]',end='')
                if lista[l][c] % 2 ==0:
                        somapares += lista[l][c]
        print(f' - LINHA.Mariz #{l}')
        print()
