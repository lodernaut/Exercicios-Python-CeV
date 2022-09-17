
def moeda(preço = 0, moeda = 'R$'):
    return f"{moeda}{preço:.2f}".replace('.',',')

#ou
'''def moeda(preço):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(preço)'''

def dobro(preço):
    return 2 * preço


def metade(preço):
    return preço / 2


def aumentarPorcentagem(preço, porcentagem):
    return preço + (preço * porcentagem / 100)


def descontoPorcentagem(preço, porcentagem):
    return preço - (preço * porcentagem / 100)
