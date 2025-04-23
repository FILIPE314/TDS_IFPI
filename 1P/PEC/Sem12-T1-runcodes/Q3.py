def main():
    pais1 = int(input().strip())
    pais2 = int(input().strip())

    if pais1 > pais2:
        paisB = pais2
        paisA = pais1
    else:
        paisB = pais1
        paisA = pais2

    ano = 0

    while True:
        if paisB > paisA: break
        ano += 1
        paisA += paisA * (2/100)
        paisB += paisB * (3/100)

    print(ano)

if __name__ == '__main__':
    main()