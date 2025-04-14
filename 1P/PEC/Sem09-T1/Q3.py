# função que verifica se os dois valores são de um quadrado ou um retângulo e retorna um resultado
def ret_or_quad(valor1,valor2):
    if valor1 == valor2:
        print('QUADRADO')
    if valor1 != valor2:
        x = (valor1 * 2) + (valor2 * 2)
        y = valor1 * valor2
        print(x,'-',y)
# função (main) que inicia e termina o programa
def main():
    # imprime uma informação na tela
    print('Digite 2 valores de um retângulo para que sua área seja calculada')
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input('Digite um valor qualquer:'))
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input('Digite um valor qualquer:'))
    # acionando a função
    ret_or_quad(num1,num2)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()