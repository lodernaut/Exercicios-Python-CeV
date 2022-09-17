def moeda(number, moeda='R$'):
    return f"{moeda}{number:.2f}"


def dobro(number, formatX=False):
    return_X = 2 * number
    return return_X if formatX is False else moeda(return_X)


def aumentoPorcentagem(number, formatX=False):
    return_X = number + (number * 35 / 100)
    return return_X if formatX is False else moeda(return_X)


def descontoPorcentagem(number, formatX=False):
    return_X = number - (number * 35 / 100)
    return return_X if formatX is False else moeda(return_X)
