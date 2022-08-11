import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
casa = float(input('Valor da casa: '))
casa1 = locale.currency(casa, grouping=True)
salário = float(input('Salário do comprador: '))
meses = int(input('Quantos Meses ? '))
prestação = casa / meses
prestação1 = locale.currency(prestação, grouping=True)
mínimo = salário *30 / 100
print(f'Para uma casa de{casa1} em {meses} Meses cada parcela fica em', end=''  )
print(f'{prestação1}')

if prestação <= mínimo:
    print('\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')
