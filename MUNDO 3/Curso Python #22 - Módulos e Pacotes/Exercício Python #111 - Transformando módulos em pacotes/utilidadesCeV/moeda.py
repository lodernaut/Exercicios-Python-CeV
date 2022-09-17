def escreva(msg):
    print("-"*(len(msg) + 18))
    print(msg.center(len(msg) + 18))
    print("-"*(len(msg) + 18))


def moeda(price, moeda='R$'):
    return f"{moeda}{price:.2f}".replace('.', ',')


def dobro(price, formatx=False):
    return_X = 2 * price
    return return_X if formatx is False else moeda(return_X)


def metade(price, formatx=False):
    return_X = price / 2
    return return_X if formatx is False else moeda(return_X)


def aumentoPorcentagem(price, aumento=0, formatx=False):
    return_X = price + (price * aumento / 100)
    return return_X if formatx is False else moeda(return_X)


def descontoPorcentagem(price, desconto=0, formatx=False):
    return_X = price - (price * desconto / 100)
    return return_X if formatx is False else moeda(return_X)


def espaçoTexto(texto):
    return f"{texto:<20}"


def resumo(price, aumento=0, desconto=0):
    escreva("Resumo do valor")
    print(espaçoTexto("Preço analisado:"), moeda(price))
    print(espaçoTexto("Dobro do preço:"), dobro(price, formatx=True))
    print(espaçoTexto("Metade do preço:"), metade(price, formatx=True))
    print(espaçoTexto(f"{aumento}% de aumento:"),
          aumentoPorcentagem(price, aumento, formatx=True))
    print(espaçoTexto(f"{desconto}% de desconto:"),
          descontoPorcentagem(price, desconto, formatx=True))
    print("-"*33)
