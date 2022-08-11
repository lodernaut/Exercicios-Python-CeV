from random import randint
v = 0
while True:
    jogador = int(input('Digite um número de 0 a 5: '))
    pc = randint(0, 5)
    soma = pc + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? P/I ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {soma}')
    print('Deu par' if soma % 2==0 else 'Deu Ímpar')
    if tipo =='P':
        if soma % 2==0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if soma % 2==1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente ...')
print(f'GAMER OVER! Você venceu {v} vezes.')


