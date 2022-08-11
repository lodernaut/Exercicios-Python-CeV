from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] Somar:
[2] Multiplicar:
[3] Maior:
[4] Novos Números:
[5] Sair do Programa:''')
    opcao = int(input('Digite sua opção: '))
    if opcao ==1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opcao ==2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif opcao ==3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}.')
    elif opcao ==4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao ==5:
        print('Finalizado...')
    else:
        print('Opção invalidade tente novamente')
    print('=-='*12)
    sleep(2)
print('Volte sempre.')
