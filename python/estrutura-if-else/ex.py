num1=int(input("Digite um numero: "))
num2=int(input("Digite outro numero: "))

operacao = input("Digite uma operação (+,-,*,/): ")

soma=num1+num2
sub=num1-num2
mult=num1*num2
div=num1/num2

if operacao=="+":
    print(soma)
elif operacao=="-":
    print(sub)
elif operacao=="*":
    print(mult)
else:
    print(div)