def area(wide, length):
    a = wide * length
    print(f"A área de um terreno {wide}x{length} é de {a}m².")


# Programa Principal.
print("Controle de terrenos.")
print("-"*23)
l = float(input("Digite a largura do terreno: "))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)
