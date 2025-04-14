# função que calcula os dias, horas e minutos pela quantidade de segundos
def dd(segundos1):
    # condição que verifica se os segundos são suficientes para fazer a operação
    if segundos1 // 60 // 60 * 24 >= 1:
        # variável que calcula o dias
        dd = ((segundos1 // 60) // 60) // 24
        # imprime o resultado formatado
        print(f'{dd}')
    # condição contraria
    else:
        # imprime uma mensagem caso os segundos não sejam suficientes para fazer a operação
        print('Segundos insuficientes para calcular dias, horas e minutos')
# função que calcula os dias, horas e minutos pela quantidade de segundos
def hh(segundos2):
    # condição que verifica se os segundos são suficientes para fazer a operação
    if (segundos2 // 60) // 60 >= 1:
        # variável que calcula as horas
        hh = (segundos2 // 60) // 60
        # imprime o resultado formatado
        print(f'{hh}')
    # condição contraria
    else:
        # imprime uma mensagem caso os segundos não sejam suficientes para fazer a operação
        print('Segundos insuficientes para calcular dias, horas e minutos')
# função que calcula os dias, horas e minutos pela quantidade de segundos
def mm(segundos3):
    # condição que verifica se os segundos são suficientes para fazer a operação
    if segundos3 >= 60:
        # variável que calcula os segundos
        mm = segundos3 // 60
        # imprime o resultado formatado
        print(f'{mm}')
    # condição contraria
    else:
        # imprime uma mensagem caso os segundos não sejam suficientes para fazer a operação
        print('Segundos insuficientes para calcular dias, horas e minutos')
# função (main) que inicia e termina o programa
def main():
    # variável que armazena dados
    segundos1 = 5184000
    # variável que armazena dados
    segundos2 = 12960000
    # variável que armazena dados
    segundos3 = 5184000
    # imprime uma mensagem na tela com o resultado dos cálculos
    dd(segundos1)
    # imprime uma mensagem na tela com o resultado dos cálculos
    hh(segundos2)
    # imprime uma mensagem na tela com o resultado dos cálculos
    mm(segundos3)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()