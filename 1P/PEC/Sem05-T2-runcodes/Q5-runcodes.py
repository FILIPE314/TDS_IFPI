# função que compara o valor da string e retorna o valor em true e false
def simbolo(caractere):
    return not 'A' <= caractere.upper() <='Z' and not '0' <= caractere <='9'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    caractere = input().strip()
    # imprimindo o resultado na tela do computador do usuário
    print(f'{simbolo(caractere)}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()