# função que compara o valor da string e retorna o valor em true e false
def letraenumero(caractere):
    return 'A' <= caractere.upper() <='Z' or '0' <= caractere <='9'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    caractere = input('Digite um caractere para saber se é verdadeiro ou falso:')
    # imprimindo o resultado na tela do computador do usuário
    print(f'O seu caractere é: {letraenumero(caractere)}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()