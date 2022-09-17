def leiaType(msg, type):
    if type == float:
        t = "real"
    elif type == int:
        t = "inteiro"
    while True:
        try:
            x = type(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print(f"\nerro! Por favor digite um número {t} válido.")
        except KeyboardInterrupt:
            print("\n\nEntrada de dado interrompida pelo usuário.",
                  f"\nNenhum dado '{t}' registrado")
            return 0
        else:
            return x


nInt = leiaType('Digite um número inteiro: ', int)
nFloat = leiaType('Digite um número real: ', float)
print("-"*45)
print(f"Inteiro: {nInt}, Real: {nFloat}")
