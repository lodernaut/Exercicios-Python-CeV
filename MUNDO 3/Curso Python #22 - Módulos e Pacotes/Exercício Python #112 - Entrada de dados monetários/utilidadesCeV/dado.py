from utilidadesCeV import moeda

def leiaDinheiro(msg):
    valor = input(msg)
    while True:
        if valor.replace('.', '').replace(',', '').isdigit() and valor.count('.') < 2 and valor.count(',') < 2:
            escreva(float(valor.replace(',', '.')))
            break
        else:
            print(f"'{valor}' inválido")
            valor = input(msg)

def escreva(msg):
    print("-"*38)
    print("Resumo do valor".center(38))
    print("-"*38)
    print(f"{f'Preço analisado:':<20}", moeda.moeda(msg))
    print(f"{f'Dobro do preço:':<20}", moeda.dobro(msg, formatX=True))
    print(f"{f'35% de aumento:':<20}", moeda.aumentoPorcentagem(msg, formatX=True))
    print(f"{f'22% de desconto:':<20}", moeda.descontoPorcentagem(msg, formatX=True))
    print("-"*38)
