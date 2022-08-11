from random import randint
pc = randint(0, 10)
palpites = 0
print('Sou sem computador acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez.')
print('ACERTOU')
print(f'Foram {palpites} palpites até acertar.')