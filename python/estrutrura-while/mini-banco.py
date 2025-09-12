print("=====Banco Python=====")

#criando arquivo para salvar os dados

def carregar_saldo():
    try:
        with open("dados_bancarios.txt", "r") as arquivo:
            return int(arquivo.read())
    except FileNotFoundError: 
        return 0
    
def salvar_saldo(saldo):
    with open("dados_bancarios.txt", "w") as arquivo:
        return arquivo.write(str(saldo))

#funções das operações 

def depositar(valor):
        
        saldo = carregar_saldo()
        saldo += valor
        salvar_saldo(saldo)
        print(f"seu saldo: {saldo:.2f}")
        return saldo


def sacar(valor):

    saldo = carregar_saldo()

    if valor > saldo:
        return print("saldo insuficiente para o saque")
    else:
        saldo = saldo -  valor
        salvar_saldo(saldo)
        print(f"seu saldo: {saldo}")
    return saldo


def consultar():
    saldo = carregar_saldo()
    print(f"seu saldo: {saldo}")

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
        depositar(valor)

    elif opcao==3:

        valor = int(input("digite o valor q quer sacar: "))
        sacar(valor)


