def ler_temp_escala():
    lista_temp = []
    lista_escala = []

    for i in range(2):
        t = float(input())
        e = input().upper()[0]
        lista_temp.append(t)
        lista_escala.append(e)
    return lista_temp, lista_escala

def fahrenheit_p_celsius(temp_f):
    # °C = (°F - 32) * (5/9)
    return (temp_f - 32) * 5/9

def celsius_p_fahrenheit(temp_c):
    # °F = (°C * (9/5)) + 32
    return (temp_c * (9/5)) + 32

def soma_temperatura(temp_1, temp_2):
    valor1, escala1 = temp_1
    valor2, escala2 = temp_2
    soma = 0

    if escala1 == escala2:
        soma = valor1 + valor2
        return round(soma, 4), escala2 # pd ser qualquer uma escala
    else:
        if escala2 == 'F':
            valor1 = celsius_p_fahrenheit(valor1)
            soma = valor1 + valor2
            return round(soma, 4), escala2 # escala da segunda temperatura
        if escala2 == 'C':
            valor1 = fahrenheit_p_celsius(valor1)
            soma = valor1 + valor2
            return round(soma, 4), escala2 # escala da segunda temperatura

def main():
    temperaturas, escalas = ler_temp_escala()

    temp1 = (temperaturas[0], escalas[0])
    temp2 = (temperaturas[1], escalas[1])

    soma = soma_temperatura(temp1, temp2)
    print(soma)

if __name__ == "__main__":
    main()