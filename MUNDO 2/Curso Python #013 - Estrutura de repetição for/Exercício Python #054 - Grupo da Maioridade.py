from datetime import date
atual = date.today().year
maior18 = 0
menor18 = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}º pessoa nasceu: '))
    idade = atual - nasc
    if idade >=18:
        maior18 += +1
    else:
        menor18 += +1
print(f'Tivemos ao todo {maior18} maiores de idade e {menor18} menos de idade.')
