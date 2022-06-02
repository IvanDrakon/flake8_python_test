import random # Biblioteca para numeros aleatórios

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Avivinhação!")
    print("*********************************")


    numero_secreto = random.randrange(1, 101) # 1 até 100
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = 0 # Enquanto o numero não for 1, 2 OU 3 ele vai ficar repetindo a pergunta, por isso que o nivel foi determinado como 0 e depois atribuido o valor do input asism o while pode rodar.
    while(nivel < 1 or nivel > 3):
        nivel = int(input("Escolha o nível: "))

        if(nivel == 1):
            total_de_tentativas = 20
        elif (nivel == 2):
            total_de_tentativas = 10
        elif (nivel == 3):
            total_de_tentativas = 5
        else:
            print("As dificuldades vão de 1 até 3.")
        


    for rodada in range(1, total_de_tentativas + 1) : # O for vai rodar o valor de rodada que vai ser definido dentro da função "for in range()"  
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou: ", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if (maior):
                print("Voce errou! Voce chutou alto...")
            elif (menor):
                print("Voce errou! Voce chutou baixo...")
            pontos_perdidos = abs (numero_secreto - chute) # O abs() transforma o valor em um valor absoluto, isto é,ignora o numero negativo pegando apenas o valor dele
            pontos = pontos - pontos_perdidos

    print("***************************")
    print("********Fim do jogo********")
    print("***************************")

if(__name__ == "__main__"):
    jogar()