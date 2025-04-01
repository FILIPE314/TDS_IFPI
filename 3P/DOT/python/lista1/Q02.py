# =============================================================================================================================================================
# Questão 2
def area(raio):
    result = 3.14 * raio ** 2
    return f'Esse é a área do círculo: {result:.2f}'
def perimetro(raio):
    result = 3.14 * 2 * raio
    return f'Esse é o perímetro do círculo: {result:.2f}'
def main():
    while True:
        try:
            raio = float(input('Digite o raio de um círculo que você queira saber o perímetro e a área: '))
            print(area(raio))
            print(perimetro(raio))
        except:
            print("\nDigite um valor válido!")
if __name__ == '__main__':
    main()