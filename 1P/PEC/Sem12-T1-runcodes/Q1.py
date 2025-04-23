def main():
    distancia = int(input().strip())

    minuto = 0
    tortuga = distancia
    lebre = 0

    while True:
        if lebre >= tortuga: break
        tortuga += 1
        lebre += 10
        minuto += 1

    print(minuto)

if __name__ == '__main__':
    main()