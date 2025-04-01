# função que calcula e retorna o valor do cálculo
def hora1(minuto1):
    x = minuto1 // 60
    return x
# função que calcula e retorna o valor do cálculo
def minuto2(minuto1):
    y = minuto1 % 60
    return y
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    minuto1 = int(input().strip())
    # guardando o resultado em variáveis e transformando para string
    hora = str(hora1(minuto1))
    minuto = str(minuto2(minuto1))
    # imprimindo o resultado na tela do computador do usuário
    print(hora+':'+minuto)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()