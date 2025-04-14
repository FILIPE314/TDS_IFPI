# função que faz um cálculo dependendo da resposta
def rest_div(resto,num,a):
    if resto == 0:
        return (9 * num) + 7
    elif resto == 1 and a == 0:
            return 'par'
    elif resto == 1 and a == 1:
            return 'ímpar'
    elif resto == 2:
        return 5 * (num * num) - (3 * num) + 42
    elif resto == 3:
        return num // 10
    elif resto == 4:
         return num ** 2
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num = int(input().strip())
    # variável que calcula e armazena dados
    resto = num % 5
    # variável que calcula e armazena dados
    a = num % 2
    # acionando a função
    print(rest_div(resto,num,a))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()