# função para calcular quantos caracteres tem em uma frase
def idade_espacial(idade):
    # imprime o resultado quando a função é acionada
    print('Você tem',idade // 2,'anos espaciais')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    idade = int(input('Digite aqui sua idade terrestre para saber sua idade ESPACIAL:'))
    # acionando a função
    idade_espacial(idade)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()