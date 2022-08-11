soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 ==0:
        soma = soma + num
        cont = cont +1
print(f'A soma de todos os  {cont}  valores solicitados é {soma}')
