# função que calcula e retorna o valor do cálculo
def area1(lado):
    return lado * lado
# função que calcula e retorna o valor do cálculo
def perimetro1(lado):
    return lado * 4
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    lado = float(input().strip())
    # guardando o resultado na variável (area)
    area = area1(lado)
    # guardando o resultado na variável (perimetro)
    perimetro = perimetro1(lado)
    # Imprimindo o resultado na tela do computador do usuário
    print(f'{area:10.4f}')
    print(f'{perimetro:10.4f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()