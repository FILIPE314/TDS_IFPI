# 2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área 
# do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
# Área = PI * r2; Perímetro = PI * 2 * r;
def area(raio):
    return 3.14 * raio **2

def perimetro(raio):
    return 3.14 * 2 * raio
    
def main():
    while True:
        try:
            raio = float(input("\nDigite o raio do círculo: "))
            print(f"\nA área do círculo de raio {raio} é: {area(raio)}")
            print(f"\nO perímetro do círculo de raio {raio} é: {perimetro(raio)}")
            break
        except:
            print("\nERRO: Digite um valor válido!")
if __name__ == "__main__":
    main()