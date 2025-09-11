#criando com arquivo

with open("teste.txt", "w")  as arquivo:
    arquivo.write("arquivo criado com sucesso")

#lendo o arquivo

with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
    
    #mostrando na tela o arquivo q foi lido

    print("conteudo do arquivo: ")
    print(conteudo)

#escrevendo no arquivo sem apagar o anterior

with open("teste.txt", "a") as arquivo:
    arquivo.write("mensagem adicionada com sucesso")