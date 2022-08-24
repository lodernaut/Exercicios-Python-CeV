from datetime import datetime
lista = dict()
lista['Nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input(f"Ano de nascimento: "))
lista['Idade'] = datetime.now().year - nascimento
lista['CTPS'] = int(
    input('Número Carteira de tabalho: [Digite  0 se não possuir]: '))
if lista['CTPS'] > 0:
    lista['Contratação'] = int(input('Ano de Contratação: '))
    salario = float(input('Salário: '))
    lista['Salário'] = f"{salario:.2f}"
    lista['Aposentadoria'] = (lista['Contratação'] - nascimento) + 35
for k, v in lista.items():
    print(f"{k}: {v}")
