# 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.

def perimetro(qtd, medida):
    return qtd * medida

def area(medida):
    return medida **2

def main():
    while True:
        try:
            lados = int(input("\nDigite o número de lados de um polígono regular(3, 4 ou 5): "))
            medida = float(input("Digite a medida do lado em cm: "))
            
            if lados not in [3, 4, 5] or medida <= 0:
                print("\nO número de lados deve ser 3, 4 ou 5 e a medida do lado deve ser maior que 0!")
                main() # Para retornar ao início em caso de erro
            else:
                print(f"\n{"="*8} Nome do polígono: {"="*8}")
                if lados == 3:
                    print(f"TRIÂNGULO! o seu perímetro é: {perimetro(lados, medida)} cm")
                elif lados == 4:
                    print(f"QUADRADO! a sua área é: {area(medida)} cm")
                elif lados == 5:
                    print(f"PENTAGONO!")
            break
        except:
            print("\nERRO: Entrada inválida, digite somente valores numéricos!")
if __name__=="__main__":
    main()