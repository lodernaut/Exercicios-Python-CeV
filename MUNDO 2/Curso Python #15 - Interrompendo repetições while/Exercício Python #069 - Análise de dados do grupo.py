tot18 = totH = totM20 =  0
while True:
    idade = int(input('Idade: '))
    genero = ' '
    while genero not in 'FM':
        genero = str(input('Gênero: F/M ')).strip().upper()[0]
    if idade >=18:
        tot18 += 1
    if genero == 'M':
        totH += 1
    if idade < 20 and genero =='F':
        totM20 += 1
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if stop == 'N':
        break
print(f'Total de pessoas com 18 anos ou +18: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados ')
print(f'Ao todo tiveram {totM20} mulheres com menos de 20 anos')
