print("=====Banco Python=====")

#saldo da conta 

saldo = 0

#funções das operações 

def depositar(deposito):

    return saldo+deposito

def sacar(saque):
    return saldo - saque

def consultar():
    return saldo   

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
        print("Seu saldo: ", consultar())
    elif opcao==2:
        depositando = int(input("digite o valor do deposito: "))
        depositar(depositando)
    elif opcao==3:
        #saque = int(input("digite o valor q quer sacar"))
        sacar()


