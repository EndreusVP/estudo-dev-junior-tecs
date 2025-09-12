print("=====Banco Python=====")

#saldo da conta 

saldo = 0

with open("dados_bancarios.txt", "w") as arquivo:

    saldo_str = str(saldo)
    arquivo.write("Seu saldo: ")
    arquivo.write(saldo_str)

#funções das operações 

def depositar(valor):
    with open("dados_bancarios.txt", "w") as arquivo:

        calculo = valor + saldo
        calculo_str = str(calculo)
        arquivo.write("Seu saldo: ")
        arquivo.write(calculo_str)


def sacar(valor):

    saldo_int = int(saldo)

    if valor > saldo_int:
        return print("saldo insuficiente para o saque")
    else:

        calculo = saldo_int - valor
        calculo_str = str(calculo)
        arquivo.write("Seu saldo: ")
        arquivo.write(calculo_str)

def consultar():
    with open("dados_bancarios.txt", "r") as arquivos:
        print("seu saldo eh : ")
        print(arquivo.read())

#valor pra entrar no laço

opcao = -1

#laço pra operar as escolhas do usuario

while opcao!=0:

    #operações do banco

    print("1 - Cosultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Sair")

    #guardando operação

    opcao=int(input("Escolha uma opcão: "))

    #saindo do laço se opcao == 0

    if opcao==0:

        print("saindo...")
        break
    
    #condiçoes das operações

    if opcao==1:

        consultar()

    elif opcao==2:

        valor = int(input("digite o valor do deposito: "))
        saldo = depositar(valor)

    elif opcao==3:

        valor = int(input("digite o valor q quer sacar: "))
        saldo = sacar(valor)


