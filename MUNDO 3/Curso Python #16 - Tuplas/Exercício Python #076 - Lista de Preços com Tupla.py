listagem = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90,
            "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99,
            "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for item in range(0, len(listagem),2):  #indo de zero até o tamanho da lista
    print(f"{listagem[item]:.<25}",f"R${listagem[item+1]:>7.2f}")