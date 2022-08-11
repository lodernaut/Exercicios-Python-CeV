cont = soma = 0
n = int(input('Digite um número [999 parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 parar]: '))
print(f'Você digitou {cont} valores e a soma deles é {soma}')