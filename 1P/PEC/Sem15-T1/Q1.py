def conversor(temp):
    return (temp - 32) * (5/9)

def comparaTemp(temp0, temp1):
    temperatura0, escala0 = temp0
    temperatura1, escala1 = temp1

    if escala0 == 'F':
        temperatura0 = conversor(temperatura0)
    if escala1 == 'F':
        temperatura1 = conversor(temperatura1)


    if temperatura1 > temperatura0:
        return temp1[0], temp1[1]
    else:
        return temp0[0], temp0[1]

def main():
    temperaturas = []
    escalas = []

    print('Insira duas temperaturas em Celcius(C) ou Fahrenheit(F):')
    while len(temperaturas) < 2:
        temp = float(input('Temperatura: ').strip())
        temperaturas.append(temp)
        escala = str(input('Escala: ').upper()[0])
        escalas.append(escala)

    temp0 = (temperaturas[0], escalas[0])
    temp1 = (temperaturas[1], escalas[1])

    maiortemp = comparaTemp(temp0, temp1)
    print('A maior temperatura é:', maiortemp)

if __name__ == "__main__":
    main()