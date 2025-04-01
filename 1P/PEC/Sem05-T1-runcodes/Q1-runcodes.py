# função que calcula e retorna o valor do cálculo
def calcular(a,b,c):
    return 2 * a + 5 * b - c
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    a = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    b = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    c = int(input().strip())
    # guardando o resultado na variável (result)
    result = calcular(a,b,c)
    # Imprimindo o resultado na tela do computador do usuário
    print(f'{result:.0f}')
# complementar da função (main) essa encerra o programa 
if __name__=='__main__':
    main()