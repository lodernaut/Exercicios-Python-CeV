cores = {'limpa': '\033[m',
         'verde': '\033[1;97;42m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;107m'}


def miniHelp(x):
    print(cores['amarelo'])
    help(x)
    print(cores['limpa'])


print(f"{cores['verde']}  Sistema de ajuda PyHelp.  {cores['limpa']}".center(68))
manual = input(
    "Digite uma função ou Biblioteca para ver seu manual: → ").strip().upper()
while manual not in 'FIM':
    miniHelp(manual.lower())
    manual = input("Função ou Biblioteca: → ").strip().upper()
print("encerrado.")
