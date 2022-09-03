def escreva(texto):
    print("~"*(len(texto)+4))
    print(f"{texto:^{len(texto)+4}}")
    print("~"*(len(texto)+4), '\n')


a = "Hello, world!"
b = "Olá, Mundo!"
c = "Framework Django."
escreva(a)
escreva(b)
escreva(c)
