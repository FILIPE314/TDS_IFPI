# função que calcula os dias, horas e minutos pela quantidade de segundos
def dd(segundos):
    # condição que verifica se os segundos são suficientes para fazer a operação
    if segundos // 60 // 60 // 24 >= 1:
        # variável que calcula o dias
        dd = ((segundos // 60) // 60) * 24
        # imprime o resultado formatado
        print(f'{dd} dias')
    # condição contraria
    else:
        # imprime uma mensagem caso os segundos não sejam suficientes para fazer a operação
        print('Segundos insuficientes para calcular dias, horas e minutos')
# função que calcula os dias, horas e minutos pela quantidade de segundos
def hh(segundos):
    # condição que verifica se os segundos são suficientes para fazer a operação
    if segundos // 60 // 60 >= 1:
        # variável que calcula as horas
        hh = (segundos // 60) % 60
        # variável que calcula os segundos
        mm = segundos % 60
        # imprime o resultado formatado
        print(f'{hh} horas')
    # condição contraria
    else:
        # imprime uma mensagem caso os segundos não sejam suficientes para fazer a operação
        print('Segundos insuficientes para calcular dias, horas e minutos')
# função que calcula os dias, horas e minutos pela quantidade de segundos
def mm(segundos):
    # condição que verifica se os segundos são suficientes para fazer a operação
    if segundos >= 60:
        # variável que calcula os segundos
        mm = segundos // 60
        # imprime o resultado formatado
        print(f'{mm} minutos')
    # condição contraria
    else:
        # imprime uma mensagem caso os segundos não sejam suficientes para fazer a operação
        print('Segundos insuficientes para calcular dias, horas e minutos')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    segundos = int(input('Coloque um número desejado de segundos para ser transformados em dias, horas e minutos respectivamente:').strip())
    # imprime uma mensagem na tela com o resultado dos cálculos
    dd(segundos)
    # imprime uma mensagem na tela com o resultado dos cálculos
    hh(segundos)
    # imprime uma mensagem na tela com o resultado dos cálculos
    mm(segundos)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()