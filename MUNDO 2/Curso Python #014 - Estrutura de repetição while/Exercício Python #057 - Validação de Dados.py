genero = str(input('Gênero F/M: ')).strip().upper()[0] #upper está pegando apenas a primeira letra
while genero not in 'MF': #como usou o upper não precisa colocar 'FfMm'
    genero = str(input('Dados inválidos. Por Favor, informe o gênero:  ')).strip().upper()[0]
print(f'Gênero {genero} registrado com sucesso.')

