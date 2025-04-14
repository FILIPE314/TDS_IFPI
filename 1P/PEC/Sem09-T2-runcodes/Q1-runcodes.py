# função que imprime uma mensagem de acordo com a resposta do ususário
def dias(resposta):
    if resposta == 1:
        print('domingo')
    elif resposta == 2:
        print('segunda-feira')
    elif resposta == 3:
        print('terça-feira')
    elif resposta == 4:
        print('quarta-feira')
    elif resposta == 5:
        print('quinta-feira')
    elif resposta == 6:
        print('sexta-feira')
    elif resposta == 7:
        print('sábado')
    else:
        print('valor inválido')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    resposta = int(input().strip())
    # imprime uma mensagem na tela com o resultado dos cálculos
    dias(resposta)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()