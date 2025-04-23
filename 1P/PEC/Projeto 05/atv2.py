from random import *

score = 0

#imprima as 3 portas e as instruções do jogo
print("Porta da Fortuna!")
print("Existe um super prêmio atrás de uma destas 3 portas! Adivinhe qual é a porta certa para ganhar o prêmio!")
print(" _____   _____   _____")
print("|     | |     | |     |")
print("| [1] | | [2] | | [3] |")
print("|    °| |    °| |    °|")
print("|_____| |_____| |_____|")
#deixe o jogador fazer 3 tentativas for attempt in range(3):
for attempt in range(3):
    print("\nEscolha uma porta (1, 2 ou 3):")

    #pegue a porta escolhida e a armazene como um número inteiro (int)

    portaEscolhida = input() 
    portaEscolhida = int(portaEscolhida)

    #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)

    portaCerta = randint(1,3)

    #mostre ao jogador qual porta ele escolheu e qual era a porta certa

    print("A porta escolhida foi a", portaEscolhida)

    print("A porta certa é a", portaCerta)

    #o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo

    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score = score + 1
    else:
        print("Que peninha!")

    print("Sua pontuação é", score)

print("Fim. Obrigado por jogar!")
print("Sua pontuação final e de", score)