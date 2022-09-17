def notas(*nota, situação=False):
    ficha = dict()
    ficha['Total'] = len(nota)
    ficha['Maior'] = max(nota)
    ficha['Menor'] = min(nota)
    ficha['Média'] = sum(nota) / len(nota)
    if situação:
        if ficha['Média'] < 5:
            ficha['situação'] = 'Ruim'
        elif ficha['Média'] >= 5 and ficha['Média'] < 7:
            ficha['situação'] = 'Razoável'
        else:
            ficha['situação'] = 'Boa'

    return ficha


resp = notas(5.5, 2.5, 9, 8.5, situação=True)
print(resp)