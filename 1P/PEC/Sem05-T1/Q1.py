# função que calcula e retorna o valor do cálculo
def calcular(a,b,c):
    return 2 * a + 5 * b - c
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    a = int(input('Se você quiser calcular 3 números dentro desta função 2 * a + 5 * b - c, digite o número que vai no lugar da letra (a):'))
    # variável que imprime uma informação na tela e armazena dados
    b = int(input('Agora digite o número que vai no lugar da letra (b):'))
    # variável que imprime uma informação na tela e armazena dados
    c = int(input('Agora digite o número que vai no lugar da letra (c):'))
    # guardando o resultado na variável (result)
    result = calcular(a,b,c)
    # imprimindo o resultado na tela do computador do usuário
    print(f'O resultado é:{result:.0f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()