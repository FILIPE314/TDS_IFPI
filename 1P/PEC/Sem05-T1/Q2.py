# função que calcula e retorna o valor do cálculo
def area1(lado):
    return lado * lado
# função que calcula e retorna o valor do cálculo
def perimetro1(lado):
    return lado * 4
# função (main) que inicia e termina o programa
def main1():
    # variável que imprime uma informação na tela e armazena dados
    lado = int(input('Para calcular a área e o perímetro de um quadrado coloque aqui quanto mede o lado desse quadrado:'))
    # guardando o resultado na variável (area)
    area = area1(lado)
    # guardando o resultado na variável (perimetro)
    perimetro = perimetro1(lado)
    # imprimindo o resultado na tela do computador do usuário
    print(f'A área desse quadrado é:{area:10.4f}')
    print(f'O perímetro desse quadrado é:{perimetro:10.4f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main1()