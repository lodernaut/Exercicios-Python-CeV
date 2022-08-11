from random import randint
from  time import  sleep
itens = ['Pedra', 'Papel', 'Tesoura']
print('''Suas opções: 
[0] Pedra.
[1] Papel.
[2] Tesoura.''')
jogador = int(input('Sua Escolha? '))
computador = randint(0,2)
print('\033[33mJo\033[m')
sleep(0.5)
print('\033[33mKen\033[m')
sleep(0.5)
print('\033[33mPô\033[m')
sleep(0.5)
print('=-='*9)
print(f'\033[36mJogador jogou {itens[jogador]}\033[m')
print(f'\033[36mComputador jogou {itens[computador]}\033[m')
print('=-='*9)
if  computador ==0 and jogador ==0 or computador ==1 and jogador ==1 or computador ==2 and jogador ==2:
    print('\033[33meita fizemos a mesma escolha!! vamos jogar outra vez...\033[m')
elif computador ==0 and jogador ==1 or computador ==2 and jogador ==0 or computador ==1 and jogador ==2:
    print('\033[33mAh você me venceu\033[m')
else:
    print('\033[33mhehe eu venci você\033[m')
