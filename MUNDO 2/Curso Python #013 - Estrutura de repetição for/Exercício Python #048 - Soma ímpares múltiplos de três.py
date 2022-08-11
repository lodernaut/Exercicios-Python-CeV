soma = cont = 0
for c in range(1,501, 2): #apenas números ímpares
    if c  % 3==0: # números divisivel por 3
        soma = soma + c # soma tá recebendo o que ela tem que é 0 + C
        #soma += c     //#É A MESMA COISA DA VARIÁVEL DE CIMA.
        cont = cont + 1  # toda vez que achar um número divisivel por 3 ele irá contar
        # soma = um acumulador normalmente soma um valor"variável"
        # cont = contador geralmente conta +1
print(f'A soma de todos os {cont} valores solicitados é {soma}')