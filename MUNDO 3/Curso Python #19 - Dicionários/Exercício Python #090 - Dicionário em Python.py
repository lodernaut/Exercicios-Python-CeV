dados_alunos = {}
dados_alunos['Nome'] = str(input('Nome: ')).strip().title()
dados_alunos['Média'] = float(input(f"Nota média de {dados_alunos['Nome']}: "))
if dados_alunos['Média'] < 5:
    dados_alunos['Siituação'] = 'Reprovado'
elif 5 <= dados_alunos['Média'] < 7:
    dados_alunos['Siituação'] = 'Recuperação'
else:
    dados_alunos['Siituação'] = 'Aprovado'
print('=-='*15)
for k,v in dados_alunos.items():
    print(f'  - {k} é igual a {v}')
