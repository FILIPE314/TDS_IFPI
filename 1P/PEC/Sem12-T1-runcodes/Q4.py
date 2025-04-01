def separaNum(num):
    if num == 0: return num
    resultado = 0
    while True:
        if num == 0: break
        if num > 0:
            digito = num % 10 
            num = num // 10
            resultado += digito
    return resultado

def main():
    dataNasc = int(input().strip())
    print(separaNum(dataNasc))

if __name__ == '__main__':
    main()