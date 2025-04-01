# função que cálcula qual o código do caráctere digitado
def cod_caractere(caractere):
    # imprime o resultado quando a função é acionada
    print(ord(caractere))
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    caractere = input()
    # acionando a função
    cod_caractere(caractere)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main() 
