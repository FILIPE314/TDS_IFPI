from random import *

jogando = True

score = 0

#imprima as 3 portas e as instruções do jogo
print("Número da Sorte!")
print("Teste sua sorte com números!")
#repetir enquanto a variável jogando estiver com o valor verdadeiro
while jogando == True:
    print("\nEscolha um número de 1 a 10:")

    #pegue a porta escolhida e a armazene como um número inteiro (int)

    nescolhido = input() 
    nescolhido = int(nescolhido)

    #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)

    ncerto = randint(1,10)

    #mostre ao jogador qual porta ele escolheu e qual era a porta certa

    print("O número escolhido foi", nescolhido)

    print("A porta certa é a", ncerto)

    #o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo

    if nescolhido == ncerto:
        print("Parabéns!")
        score = score + 1
    else:
        print("Que peninha!")

    if score == 21:
        print("Você ganhou o jogo!")
        jogando = False
    else:
        jogando = True

    #pergunte ao jogador se ele quer continuar jogando
    print("\nVoce quer jogar de novo? (s/n)")
    reposta = input()

    #se a resposta for'nao' o jogador não continuará jogando, caso contrário continua o jogo
    if reposta.lower() =='n' or reposta.lower() == 'NAO':
        jogando = False
    else:
        jogando = True

print("Fim. Obrigado por jogar!")
print("Sua pontuação final e de", score)