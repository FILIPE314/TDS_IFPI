# função que cálcula quantas sílabas tem um uma palavra
def silabas(palavra):
    # imprime o resultado quando a função é acionada
    print('Essa palavra tem:',len(palavra),'sílabas')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    palavra = input('Digite uma palavra par que possamos cálcular quantas sílabas ela tem:')
    # acionando a função
    silabas(palavra)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()