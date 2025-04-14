# função que divide um valor por 2 para saber se é par ou ímpar
def p_imp(num):
    return num % 2
# função(condicional) que verifica se o número é par ou ímpar e adiciona o valor dependendo do caso
def calc(par_ou_impar,num):
    if par_ou_impar == 0:
        return num + 5
    else:
        return num + 8
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num = float(input('Coloque um número para saber se é ímpar ou par caso seja ímpar o número ira ser somado com 8 e se for par sera somado com 5:'))
    # variável que armazena dados
    par_ou_impar = p_imp(num)
    # imprime uma mensagem na tela com o resultado da função
    print(calc(par_ou_impar,num))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()