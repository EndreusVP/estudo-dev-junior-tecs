opcao = -1

#funções pra adicionar usuarios e ler arquivo

def adicionar_usuario():
    with open("usuario.txt", "a") as arquivo:
        nome = input("Digite o nome de usuario: ")
        idade = input("Digite a idade do ususario: ")

        #escrevendo os dados no arquivo

        arquivo.write(f"nome: {nome} | idade: {idade}\n")

def mostrar_usuarios():
    with open("usuario.txt", "r") as arquivo:
        print(arquivo.read())

#laço para adcionar usuarios

while opcao != 0:

    #menu

    print("=====Cadastro de usuarios=====")

    print("1 - adcionar usuario")
    print("2 - ver usuarios")
    print("0 - sair")

    #guardando escolha do usuario

    opcao = int(input("escolha uma opção"))

    #saindo do laço caso opcao == 0

    if opcao == 0:
        print("saindo...")
        break

    #condições para mostrar oq foi escolhido pelo usuario

    if opcao == 1:
        adicionar_usuario()
    elif opcao == 2:
        mostrar_usuarios()
    else:
        print("opção invalida...")