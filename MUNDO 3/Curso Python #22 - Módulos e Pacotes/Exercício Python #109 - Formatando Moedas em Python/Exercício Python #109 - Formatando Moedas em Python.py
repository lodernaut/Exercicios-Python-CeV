import moeda
# ou from moeda import dobro, metade, aumentarPorcentagem, descontoPorcentagem

price = float(input("Digite o preço: R$ "))
print(f"Dobro de {moeda.moeda(price)} é: {moeda.dobro(price,formatx=True)}")
print(f"Metade de {moeda.moeda(price)} é: {moeda.metade(price,formatx=True)}")
print(
    f"Aumentando 10% de {moeda.moeda(price)} é: {moeda.aumentarPorcentagem(price, 10,formatx=True)}")
print(
    f"Desconto de 10% de {moeda.moeda(price)} é: {moeda.descontoPorcentagem(price, 10,formatx=True)}")
print(
    f"Aumentando 13% de {moeda.moeda(price)} é: {moeda.aumentarPorcentagem(price, 13,formatx=True)}")