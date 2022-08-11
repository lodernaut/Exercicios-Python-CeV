n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2
if media < 5:
    print(f'Média é {media} o aluno está reprovado.')
elif media >=5 and media < 7:
    print(f'Média é {media} aluno está de recuperacão.')

else:
    print(f'Média é {media} aluno está aprovado.')



