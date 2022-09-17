from time import sleep

cadastradosPath = r"MUNDO 3\Curso Python #23 - Tratamento de Erros e Exceções\Exercício Python #115a - Criando um menu em Python\cadastrados.txt"

cor = {
    'vermelho' : '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'ciano': '\033[1;36m',
    'magenta': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'branco': '\033[1;37m',
    'reset': '\033[1;0;0m',
    'reverso': '\033[1;2m',
    'bgpreto': '\033[1;40m',
    'bgvermelho': '\033[1;41m',
    'bgverde': '\033[1;42m',
    'bgamarelo': '\033[1;43m',
    'bgazul': '\033[1;44m',
    'bgmagenta': '\033[1;45m',
    'bgciano': '\033[1;46m',
    'bgbranco': '\033[1;47m',
    'limpa': '\033[m'}

def header(title):
    print("-"*58)
    print(f"{cor['magenta']}{title}{cor['limpa']}".center(64))
    print("-"*58)


def menu(menuName):
    header("Menu princial.")
    while True:
        print("﹏"*30)
        for i, option in enumerate(menuName):
            print(f"-→ {cor['amarelo']}[{i+1}]{cor['limpa']} - {cor['amarelo']}{option}{cor['limpa']}".center(len(option) + 37))
        try:
            option = int(input("Digite um dos números acima referente a opção desejada: "))
            print("﹏"*30)
        except (ValueError, TypeError):
            print("﹏"*30)
            print(f"{cor['amarelo']}Apenas número inteiro para definir a opção.{cor['limpa']}")
            sleep(2)
        except KeyboardInterrupt:
            print(f"\n{cor['vermelho']}Interrompido pelo usuário.{cor['limpa']}")
            return 3
        else:
            if option == 1:
                header("usuários cadastrados")
                with open(cadastradosPath, 'r') as users:
                    print(users.read())

            elif option == 2:
                header("Cadastrar novo usuário")
                nome = str(input("Nome: "))
                idade = leiaInt("Idade: ")
                with open(cadastradosPath, 'a+') as newRegistration:
                    newRegistration.write(f"{nome:<20}{idade} anos\n")

            elif option == 3:
                print("Encerrando sistema... Até logo!")
                break
            else:
                print(f"{cor['vermelho']}Opção inexistente{cor['limpa']}")
                sleep(2)


def leiaInt(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro: apenas números inteiros para definir idade\033[m")
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário",
                  f"\nencerrando o programa.")
            return 0
        else:
            return x
