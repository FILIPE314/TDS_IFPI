def separaNum(num):
    if num == 0: return num
    invertido = ''
    contador = 0
    while True:
        if num == 0: break
        if num > 0:
            digito = num % 10 
            num = num // 10
            invertido = invertido + str(digito)
            contador+=1
    return int(invertido)

def main():
    num = int(input().strip())
    print(separaNum(num))

if __name__ == '__main__':
    main()