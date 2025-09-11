#criando um arquivo

with open("dados.txt", "a") as arquivo:
    nome = input("digite seu nome: ")
    idade = input("digite sua idade: ")

    #escrevendo os dados no arquivo

    arquivo.write(f"nome do usuario: {nome} | idade do usuario: {idade}\n")

#lendo os dados dos usuarios

with open("dados.txt", "r") as arquivo:

    print("=====usuarios cadastrados=====")

    conteudo = arquivo.read()
    print(conteudo)