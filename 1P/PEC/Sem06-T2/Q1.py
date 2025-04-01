# função para calcular quantos caracteres tem em uma frase
def caractere(frase):
    # imprime o resultado quando a função é acionada
    print('Essa frase tem exatamente:', len(frase),'caracteres')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    frase = input('Digite aqui uma frase para que possa ser calculado quantos caracteres tem na frase:')
    # acionando a função
    caractere(frase)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()