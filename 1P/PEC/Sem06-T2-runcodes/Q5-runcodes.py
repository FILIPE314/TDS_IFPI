# função que calcula (celsius) para (fahrenheit)
def fahrenheit(celsius):
    # retorna o valor calculado
    return (celsius * (9 / 5)) + 32
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    celsius = float(input().strip())
    # imprime uma mensagem(formatada) na tela com o resultado dos cálculos
    print(f'{fahrenheit(celsius):.2f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()