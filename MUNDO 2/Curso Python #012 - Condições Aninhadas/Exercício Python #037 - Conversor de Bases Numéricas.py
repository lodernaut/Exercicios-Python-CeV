num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases abaixo para conversão: '
      '\n[1] Converter para BINÁRIO. '
      '\n[2] Converter para OCTAL. '
      '\n[3] Converter para HEXADECIMAL.'
      '\n[4] Para converter todas opções acima.')
opção = int(input('Sua Opção: '))

if opção == 1:
    print(f'{num} --> Convertido para Binário é igual a: \033[32m{bin(num)[2:]}\033[m')
elif opção == 2:
    print(f'{num} --> Convertido para Octal é igual a: \033[32m{oct(num)[2:]}\033[m')
elif opção == 3:
    print(f'{num} --> Convertido para Hexadecimal é igual a: \033[32m{hex(num)[2:]}\033[m')
elif opção == 4:
    print(f'{num} --> Binário:\033[32m{bin(num)[2:]}\033[m // Octal:\033[32m{oct(num)[2:]}\033[m // Hexadecimal:\033[32m{hex(num)[2:]}\033[m')
else:
    print('\033[31mOpção não encontrada tente novamente " \033[32m1. 2 ou 3 "\033[m')

quit()
