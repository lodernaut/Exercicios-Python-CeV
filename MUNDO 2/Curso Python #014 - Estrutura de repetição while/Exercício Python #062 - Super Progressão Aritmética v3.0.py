pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
total = 0
mais = 10 #simulando que o usuário digitou mais 10 termos. começo do programa.
while mais !=0: #para encerrar a contagem/programa
    total = total + mais
    while cont <= total: #total de termos que será mostrado
        print(f'{termo}',end=' ')
        termo += r
        cont += 1
    print('PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {} termos mostrandos.')