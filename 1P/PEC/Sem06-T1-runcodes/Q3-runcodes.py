# função que cálcula quantos segundos sobram de acordo com a quantidade de segundos
def seg(segundos):
    # retorna o valor calculado 
    return str(segundos % 60)
# função que cálcula quantos minutos tem de acordo com a quantidade de segundos
def min(segundos):
    # retorna o valor calculado 
    return str(segundos // 60 % 60)
# função que cálcula quantos minutos tem de acordo com a quantidade de segundos
def hr(segundos):
    # retorna o valor calculado
    return str(segundos // 60 // 60)
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    segundos = int(input().strip())
    # imprimindo uma mensagem na tela com o resultado dos cálculos
    print(hr(segundos)+':'+min(segundos)+':'+seg(segundos))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()