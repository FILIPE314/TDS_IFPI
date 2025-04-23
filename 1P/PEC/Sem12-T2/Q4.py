def main():
    numDigitado = int(input('Digite um número: '))
    cont = 0
    i = 1

    while i < (numDigitado + 1):
        divisao = numDigitado % i
        if divisao == 0:
            cont += 1
        i += 1    
    if cont == 2: 
        print('True, é primo')
    else:
        print('False, não é primo')

if __name__ == "__main__":
    main()