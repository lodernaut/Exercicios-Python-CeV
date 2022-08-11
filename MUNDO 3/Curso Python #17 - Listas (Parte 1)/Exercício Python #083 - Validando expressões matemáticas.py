expre = str(input('Digite uma Expressão: '))
cont = 0
for x in expre:
    if x =='(':
        cont += 1
    elif x == ')':
        cont -= 1
    else:
        cont < 0
        print('Expressão Invalida.')
        exit(0)
if cont !=0:
    print('Expressão Invalida.')
else:
    print('Expressão Válida.')