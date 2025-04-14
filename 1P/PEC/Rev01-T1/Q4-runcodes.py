# função que calcula as horas, minutos e segundos pela quantidade de segundos
def hhmmss(segundos):
    # condição que verifica se os segundos são suficientes para fazer a operação
    if 359999 >= segundos >= 3540:
        # variável que calcula os dias
        hh = (segundos // 60) // 60
        # variável que calcula as horas
        mm = (segundos // 60) % 60
        # variável que calcula os segundos
        ss = segundos % 60
        # imprime o resultado formatado
        print(f'{hh:02.0f}:{mm:02.0f}:{ss:02.0f}')
    # condição que verifica se os segundos são suficientes para fazer a operação
    elif 3540 > segundos >= 60:
        # variável que calcula as horas
        mm = segundos // 60
        # variável que calcula os segundos
        ss = segundos % 60
        if mm == 60:
            # imprime o resultado formatado
            print(f'01:00:0{ss}')
        else:
            # imprime o resultado formatado
            print(f'00:{mm:02.0f}:{ss:02.0f}')
    # condição que verifica se os segundos são suficientes para fazer a operação
    elif 60 > segundos >= 10:
        # variável que calcula os segundos
        ss = segundos % 60
        # imprime o resultado formatado
        print(f'00:00:{ss:02.0f}')
    # condição que verifica se os segundos são suficientes para fazer a operação
    elif 10 > segundos >= 1:
        # imprime o resultado formatado
        print(f'00:00:0{segundos}')
    # condição contraria
    else:
        # imprime uma mensagem caso os segundos não sejam suficientes para fazer a operação
        print('00:00:00')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    segundos = int(input())
    # imprime uma mensagem na tela com o resultado dos cálculos
    hhmmss(segundos)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()