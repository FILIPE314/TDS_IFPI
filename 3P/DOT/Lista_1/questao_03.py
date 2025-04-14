# 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar 
# o valor correspondente em graus Celsius.
# Fórmula: C = ((F-32)/9)*5

def celsius(temp):
    return ((temp-32) / 9)*5

def main():
    while True:
        try:
            temperatura = float(input("\nDigite a temperatura em graus Fahrenheit: "))
            print(f"\nA temperatura {temperatura}°F corresponde  a {celsius(temperatura)}°C")
            break
        except:
            print("\nERRO: Temperatura inválida, tente novamente!")
if __name__ == "__main__":
    main()
