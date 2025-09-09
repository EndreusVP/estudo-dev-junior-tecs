nome=str(input("igite o nome de usuario: "))
senha=int(input("Digite a senha: "))

if nome=="admin":
    if senha==1234:
        print("Login executado")
    else:
        print("senha incorreta")
else:
    print("usuario nao encontrado")