def main():
    n = int(input('Digite a quantidade de termos que deseja mostrar: '))
    a = 0
    b = 1
    c = 0 # Uma variável temporária para armazenar o próximo termo da sequência 
    cont = 0

    while cont < n:
        if cont == n - 1: # Último termo
            print(f'{c}', end='')
        else:
            print(f'{c}', end=', ')

        a = b # pra atualizar o valor de a com o valor atual de b
        b = c # pra atualizar o valor de b com o valor atual de c
        c = a + b
        cont += 1

if __name__ == "__main__":
    main()