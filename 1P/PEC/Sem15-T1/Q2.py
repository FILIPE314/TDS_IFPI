def conversor(temp, escalaAt):
    if escalaAt.upper() == 'F':
        # F -> C
        return (temp - 32) * (5/9)
    else:
        # C -> F
        return (temp * (9/5)) + 32

def somaTemp(temp0, temp1):
    temperatura0, escala0 = temp0
    temperatura1, escala1 = temp1

    if escala0 != escala1:
        temperatura0 = conversor(temperatura0, escala0)

    return round((temperatura0 + temperatura1), 4), escala1

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

    print('A soma entre as duas temperaturas é:', somaTemp(temp0, temp1))

if __name__ == "__main__":
    main()