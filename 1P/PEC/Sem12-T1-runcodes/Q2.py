def main():
    carro = float(input().strip())

    mes = 0
    poupanca = 10000

    while True:
        if poupanca >= carro: break
        mes += 1
        poupanca += poupanca * (0.7/100)
        carro += carro * (0.4/100)

    print(mes)

if __name__ == '__main__':
    main()