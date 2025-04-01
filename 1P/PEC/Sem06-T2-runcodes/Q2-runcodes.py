# função que arredonda um número real
def arredonda(numero):
    # imprime o resultado quando a função é acionada
    print(round(numero))
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    numero = float(input().strip())
    # aaciona a função
    arredonda(numero)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()