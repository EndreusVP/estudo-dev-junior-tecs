#importanto random pra randomizar numeros
import random

print("=====jogo de adivinhação=====")

#variaveis
numero = random.randint(1, 20)
acertou = False
tentativa = 0

#testando se acertou ou nao
while acertou == False:
    print("=====adivinhe o numero=====")

    chute = int(input("chute um numero: "))

    if chute == numero:
        print("vc acertou!!! parabens!!!")
        print(f"tentativas: {tentativa}")
        acertou = True
    elif chute > numero:
        print("o numero eh menor")
        tentativa += 1
    elif chute < numero:
        print("o numero eh maior")
        tentativa += 1
    elif chute > 20:
        print("o jogo vai so de 1 ate 20")
        print("tente novamente")
        print("essa tentaiva nao afetara seu score")

print("obgd por jogar")

