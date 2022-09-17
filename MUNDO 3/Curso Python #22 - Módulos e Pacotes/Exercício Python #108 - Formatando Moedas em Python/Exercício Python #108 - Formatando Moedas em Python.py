import moeda
# ou from moeda import dobro, metade, aumentarPorcentagem, descontoPorcentagem

price = float(input("Digite o preço: R$ "))
print(f"Dobro de {moeda.moeda(price)} é: {moeda.moeda(moeda.dobro(price))}")
print(f"Metade de {moeda.moeda(price)} é: {moeda.moeda(moeda.metade(price))}")
print(
    f"Aumentando 10% de {moeda.moeda(price)} é: {moeda.moeda(moeda.aumentarPorcentagem(price, 10))}")
print(
    f"Desconto de 10% de {moeda.moeda(price)} é: {moeda.moeda(moeda.descontoPorcentagem(price, 10))}")
