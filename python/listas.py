#variaveis 
i= 0

#listas
lista = []

#laço para inserir itens na lista 
while i < 5:
    item = input("insira um item na lista: ")
    lista.append(item)
    i += 1

#laço para mostrar itens da lista
for item in lista :
    print("-", item)

