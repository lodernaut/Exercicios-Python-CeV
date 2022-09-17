import moeda
# ou from moeda import dobro, metade, aumentarPorcentagem, descontoPorcentagem

price = float(input("Digite o preço: R$ "))
print(f"Dobro de R${price} é: R${moeda.dobro(price)}")
print(f"Metade de R${price} é: R${moeda.metade(price)}")
print(
    f"Aumentando 10% de R${price} é: R${moeda.aumentarPorcentagem(price, 10)}")
print(
    f"Desconto de 10% de R${price} é: R${moeda.descontoPorcentagem(price, 10)}")
