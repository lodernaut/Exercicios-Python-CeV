palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'TRABALHAR')
for c in palavras:
    print(f'\nNa palavra {c} temos: ',end='')
    for letra in c:
        if letra.lower() in'aeiou':
            print(f'{letra} ',end='') # se colocar letra.lower() passa a mostrar em minúsculo

