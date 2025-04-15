# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
# - para homens : (72.7 * h) – 58
# - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).

def peso_ideal(altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    elif sexo == 2:
        return (72.7 * altura) - 58
    
def main():
    while True:
        try:
            altura = float(input("\nDigite a sua altura em metros: "))
            sexo = int(input("Digite o seu sexo (1: feminino, 2: masculino): "))
            
            if altura <= 0 or sexo not in [1, 2]:
                print("\nERRO: Altura deve ser maior que zero e o sexo tem que ser 1 ou 2!")
                main()
            else:
                print(f"O seu peso ideal é: {peso_ideal(altura, sexo):.2f}")
            break
        except:
            print("\nERRO: Digite somente valores numéricos!")
if __name__=="__main__":
    main()
