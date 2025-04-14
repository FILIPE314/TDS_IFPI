# função condicional que retorna um resultado dependendo da resposta do ususário
def impar_ou_par(numero):
    # condicional(verdadeira) que verifica o resultado
    if numero % 2 == 1:
        # retorna o resutado caso seja esssa opção
        return 'True'
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return 'False'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    numero = int(input('Coloque um número para saber se é ímpar ou par caso seja ímpar ira aparecer (True), e se for par vai aparecer (False):'))
    # imprime uma mensagem na tela com o resultado da função
    print('Seu número é:',impar_ou_par(numero))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()