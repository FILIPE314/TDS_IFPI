def ler_temp_escala():
    lista_temp = []
    lista_escala = []

    for i in range(2): # mudar esse 2 depois?
        t = float(input())
        e = input().upper()[0]
        lista_temp.append(t)
        lista_escala.append(e)
    return lista_temp, lista_escala

def fahrenheit_p_celsius(temp_f):
    # °C = (°F - 32) * (5/9)
    return (temp_f - 32) * 5/9

def comparar_temperatura(temp_1, temp_2):
    valor1, escala1 = temp_1 # desempacotar a tupla em duas variáveis
    valor2, escala2 = temp_2 

    # se °F, transformar em °C
    if escala1 == 'F':
        valor1 = fahrenheit_p_celsius(valor1) 
    if escala2 == 'F':
        valor2 = fahrenheit_p_celsius(valor2)

    if valor1 > valor2:
        return temp_1 # retornar a tupla 
    else:
        return temp_2

def main():
    temperaturas, escalas = ler_temp_escala()

    temp1 = (temperaturas[0], escalas[0])
    temp2 = (temperaturas[1], escalas[1])

    print(comparar_temperatura(temp1, temp2))

if __name__ == "__main__":
    main()