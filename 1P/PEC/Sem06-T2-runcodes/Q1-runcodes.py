# função para calcular quantos caracteres tem em uma frase
def caractere(frase):
    # imprime o resultado quando a função é acionada
    print(len(frase))
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    frase = input().strip()
    # aciona a função
    caractere(frase)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()