def leiaInt(num):
    while True:
        print('-' *45)
        x = input(num).strip()
        if x.isnumeric() is False:
            print('\033[1;3;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return x


n = leiaInt('Digite um número: ')
print(f"Válido, foi digitado o número: {n}")