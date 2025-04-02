# =============================================================================================================================================================
# Questão 10 letra a
def maior(num):
    list = []
    list.append(num)
    return f'O maio número é: {max(list)}'
def main():
    print('Digite 4 números a seguir para saber qual o maior deles: ')
    try:
        for i in range(4):
            num = int(input(f'Número {i + 1}: '))
        print(maior(num))
    except:
        print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()
# Questão 10 letra b
def maximo(num1, num2, num3, num4):
    lista = [num1, num2, num3, num4]
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return f'O maior número da série é: {maior}'
def main():
    print('Digite 4 séries de números contendo 4 numeros cada série para saber o maior numero de cada serie')
    i = 0
    while i < 4:
        i += 1
        list_global = []
        try:
            print(f'Números da série A{i}')
            num1 = int(input(f'Número {i}: '))
            num2 = int(input(f'Número {i}: '))
            num3 = int(input(f'Número {i}: '))
            num4 = int(input(f'Número {i}: '))
            print(maximo(num1, num2, num3, num4))
            list_global.append(maximo(num1, num2, num3, num4))
        except:
            i -= 1
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()