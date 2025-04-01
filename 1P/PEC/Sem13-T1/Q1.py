def ler_numeros(n):
    numeros = []    
    for i in range(10):
        numeros.append(int(input()))       
    return numeros

def soma_numeros(n):
    return sum(n)

def mult_numeros(n):
    mult = 1    
    for i in n:
        mult *= i       
    return mult

def main():
    numeros = ler_numeros(10)
    soma = soma_numeros(numeros)
    multiplicacao = mult_numeros(numeros)

    print(numeros)
    print(f'{soma:.0f}')
    print(f'{multiplicacao:.0f}')

if __name__ == "__main__":
    main()