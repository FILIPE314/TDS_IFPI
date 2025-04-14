# função que lê mostra quantas sílabas tem um uma palavra
def silabas(palavra):
    # imprime o resultado quando a função é acionada
    print(len(palavra))
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    palavra = input().strip()
    # acionando a função
    silabas(palavra)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()