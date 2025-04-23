# função que divide o número por 3 e por 5
def div(numero):
    if numero // 3 == 0 and numero // 5 == 0:
        return 'FIZZBUZZ'
    elif numero // 3 == 0:
        return 'FIZZ'
    elif numero // 5 == 0:
        return 'BUZZ'
    else:
        return numero
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    numero = int(input('Digite um número para saber se é FIZZ,BUZZ ou FIZZBUZZ:'))
    # imprimindo o resultado na tela do computador do usuário
    print(div(numero))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()