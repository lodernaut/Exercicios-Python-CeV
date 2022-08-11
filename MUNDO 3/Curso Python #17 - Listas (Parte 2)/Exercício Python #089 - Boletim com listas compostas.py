ficha = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2],media])
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if stop == 'N':
        break
print('=-='*26)
print(f'1{"No.":<4}{"Nome:":<10}{"Média:":>8}')
print('=-='*26)

for i, a, in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}') #i = No.  #a[0] = Nome:  #a[2] = Média:
while True:
    print('=-=' * 26)
    opc = int(input('Digite sua opção: '))
    if opc == 999:
        break
        print('FINALIZADO')
    if opc <= len(ficha) -1: #pq o primeiro aluno é o 0
        print(f'Notas de {ficha[opc][0]} é {ficha[opc][1][0]} e {ficha[opc][1][1]} ')
print('Volte Sempre.')