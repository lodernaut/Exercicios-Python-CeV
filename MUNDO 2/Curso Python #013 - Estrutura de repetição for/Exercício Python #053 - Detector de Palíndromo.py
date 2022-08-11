frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split() #dividir a frase
junto = ''.join(palavras) #limpando espaços internos
# proximo passo colocando str de trás pra frente.
inverso = junto[::-1] # 1º: significa que tá começando do inicio # 2º: terminar no fim #-1 é de trás pra frente.
print(f'O inverso de "{junto}." é "{inverso}."')
if inverso == junto:
    print('Temos um palíndro')
else:
    print('A Frase digitada não é um palíndromo.')
