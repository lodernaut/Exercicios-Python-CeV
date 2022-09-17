from package import menu


cadastradosPath = r"MUNDO 3\Curso Python #23 - Tratamento de Erros e Exceções\Exercício Python #115a - Criando um menu em Python\cadastrados.txt"
with open(cadastradosPath, 'a+') as cadastrados:
    cadastrados.write("")
menu.menu(["Ver cadastrados", "Cadastrar novo usuário", "Encerrar programa"])
