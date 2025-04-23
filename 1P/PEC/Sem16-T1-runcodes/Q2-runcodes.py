# Função para converter as temperaturas para Kelvin
def converter_para_kelvin(temp, escala):
    if escala.lower() == 'c':  # Celsius para Kelvin
        return temp + 273.15
    elif escala.lower() == 'f':  # Fahrenheit para Kelvin
        return (temp - 32) * 5/9 + 273.15
    elif escala.lower() == 'k':  # Já está em Kelvin
        return temp
    else:
        raise ValueError("Escala inválida. Use 'C' para Celsius, 'F' para Fahrenheit ou 'K' para Kelvin.")
    
meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

# Função para calcular a média anual em Kelvin
def calcular_media_anual(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Função para exibir as temperaturas acima da média, junto com o mês
def exibir_temperaturas_acima_da_media(temperaturas, media_anual):
    
    print(f"\nTemperaturas acima da média anual ({media_anual:.2f} K):")
    for i, temp in enumerate(temperaturas):
        if temp > media_anual:
            print(f"{meses[i]}: {temp:.2f} K")

def main():
    temperaturas_kelvin = []
    
    # Loop para coletar as temperaturas de cada mês
    for i in range(12):
        temp = float(input())
        escala = input()
        temperatura_kelvin = converter_para_kelvin(temp, escala)
        temperaturas_kelvin.append(temperatura_kelvin)
    
    # Calcula a média anual das temperaturas em Kelvin
    media_anual = calcular_media_anual(temperaturas_kelvin)

    # Calcula a média anual das temperaturas em Graus
    media_anual = calcular_media_anual(temperaturas_kelvin)

    
    # Exibe as temperaturas acima da média anual
    for i, temp in enumerate(temperaturas_kelvin):
        if temp > media_anual:
            print(f"{meses[i]}: {converter_para_kelvin(temp, 'C'):.2f} °C")
            
    # Exibe as temperaturas acima da média anual em Fahrenheit
    print("\nTemperaturas acima da média anual (em Fahrenheit):")
    for i, temp in enumerate(temperaturas_kelvin):
        if temp > media_anual:
            print(f"{meses[i]}: {converter_para_kelvin(temp, 'F'):.2f} °F")

    # Exibe as temperaturas acima da média anual em Kelvin
    print("\nTemperaturas acima da média anual (em Kelvin):")
    for i, temp in enumerate(temperaturas_kelvin):
        if temp > media_anual:
            print(f"{meses[i]}: {temp:.2f} K")
            
    # Exibe as temperaturas acima da média an
    exibir_temperaturas_acima_da_media(temperaturas_kelvin, media_anual)

if __name__ == "__main__":
    main()