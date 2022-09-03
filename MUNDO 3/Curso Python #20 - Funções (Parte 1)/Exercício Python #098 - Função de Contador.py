from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("=-="*20)
    print(f"Contagem de ínicio {i} até o fim {f} pulando {p}.")
    if i < f:
        cont = i
        while cont <= f:
            print(f" → {cont}", end='',flush=True)
            sleep(0.2)
            cont += p
        print(" Fim")
    else:
        cont = i
        while cont >= f:
            print(f" → {cont}", end='',flush=True)
            sleep(0.2)
            cont -= p
        print(" Fim")

    # Programa Principal.
contador(1, 10, 1)
contador(10, 0, 2)
print("=-="*20)
print("Agora é sua vez de personalizar a contagem.")
inicio = int(input("ínicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
