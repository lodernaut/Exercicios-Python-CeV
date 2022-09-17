
def moeda(preço = 0, moeda = 'R$'):
    return f"{moeda}{preço:.2f}".replace('.',',')

#ou
'''def moeda(preço):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(preço)'''

def dobro(preço, formatx=False):
    res =  2 * preço
    return res if formatx is False else moeda(res)
    #ou return res if not formatx else moeda(res) 


def metade(preço, formatx=False):
    res =  preço / 2
    return res if formatx is False else moeda(res)


def aumentarPorcentagem(preço, porcentagem, formatx=False):
    res = preço + (preço * porcentagem/ 100)
    return res if formatx is False else moeda(res)


def descontoPorcentagem(preço, porcentagem, formatx=False):
    res = preço - (preço * porcentagem / 100)
    return res if formatx is False else moeda(res)