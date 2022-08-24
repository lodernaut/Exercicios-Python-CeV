dados = dict()
cadastros = list()
listanomemulher = list()
somaidade = 0
while True:
    dados['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['Gênero'] = str(input('Gênero: ')).strip().upper()[0]
        if dados['Gênero'] in 'MF':
            break
        print('Por favor, Digite apenas F ou M.')
    if dados['Gênero'] in 'F':
        listanomemulher.append(dados['Nome'])
        dados['idade'] = int(input('Idade: '))
        somaidade += dados['idade']
        cadastros.append(dados.copy())
        dados.clear()
    while True:
        stop = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if stop in 'SN':
            break
        print('Por favor, Digite apenas F ou M.')
    if stop == 'N':
        break
print(f"Quantidade de pessoas cadastradas {len(cadastros)}")
média = somaidade / len(cadastros)
print(f"Média de idade dos Cadastrados: {média:.1f}")
print(f"Lista de Nome do Gênero feminino Cadastrado:",', '.join(listanomemulher))
print('Lista de pessoas com a idade acima da média')
for i,c in enumerate(cadastros):
    if cadastros[i]['idade'] >= média:
        values = ' '.join(map(str, cadastros[i].values()))
        keys = ' '.join(cadastros[i])
        items = ' '.join(f'{key}: {value:<2}|' for key, value in cadastros[i].items())
        print(items)
print('encerrado.')

