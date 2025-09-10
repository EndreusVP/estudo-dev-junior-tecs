#função para as operações

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b==0:
        return "dx de ser burro, 0 nao divide"
    return a/b
    
opcao=1

while opcao!=0:

    print("===== calculadora =====")
    
    #escolhendo a operação

    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")

    opcao=int(input("escolha uma opção: "))

    #saindo se a opcao 0 for escolhida

    if opcao==0:
        print("saindo...")
        break

    #inserção dos numeros

    num1=int(input("escolha um numero: "))
    num2=int(input("escolha outro numero: "))

    #condições para os calculos

    if opcao==1:
        print("resultado: ",somar(num1,num2))
    elif opcao==2:
        print("resultado :",subtrair(num1,num2))
    elif opcao==3:
        print("resultado :",multiplicar(num1,num2))
    elif opcao==4:
            print("resultado :",dividir(num1,num2))
    else:
        print("se caiu aq eh porq fez alguma merda")

