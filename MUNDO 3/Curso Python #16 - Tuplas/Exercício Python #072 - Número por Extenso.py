color = ('\033[35m','\033[m')
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'{color[0]}NÚMEROS EM EXTENSOS.{color[1]}'.center(25))
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if n < 0 or n > 20:
        print('Erro!')
        n = int(input('Digite um número ENTRE 0 a 20: '))
        if n < 0 or n > 20:
            print('Erro!')
    else:
        if 0 <= n <=20:
            print(f'{color[0]}{ext[n]}{color[1]}')
        stop = ' '
        while stop not in 'SN':
            stop = str(input('Quer Continuar? S/N: ')).strip().upper()[0]
        if stop == 'N':
            break
print(f'{color[0]}PROGRAMA ENCERRADO.{color[1]}'.center(25))