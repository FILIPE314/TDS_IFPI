# função que compara o valor da string e retorna o valor em true e false
def letra(caractere):
    return 'A' <= caractere.upper() <='Z'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    caractere = input().strip()
    # imprimindo o resultado na tela do computador do usuário
    print(f'{letra(caractere)}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()