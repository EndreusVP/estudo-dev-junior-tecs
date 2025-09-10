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

    break;

    #inserção dos numeros

    num1=int(input("escolha um numero: "))
    num2=int(input("escolha outro numero: "))

    #condições para os calculos

    if opcao==1:
        print("resultado :",num1+num2)
    elif opcao==2:
        print("resultado :",num1-num2)
    elif opcao==3:
        print("resultado :",num1*num2)
    elif opcao==4:
        if num2==0:
            print("calculo impossivel, faz essa porra direito krlh")
        else:
            print("resultado :",num1/num2)
    else:
        print("se caiu aq eh porq fez alguma merda")

