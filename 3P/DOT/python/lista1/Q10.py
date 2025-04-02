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
def maximo(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior
def maior(list_A, list_B, list_C, list_D):
    return  f'\nO maior número da serie A é: {maximo(list_A)}\n' + \
            f'O maior número da serie B é: {maximo(list_B)}\n' + \
            f'O maior número da serie C é: {maximo(list_C)}\n' + \
            f'O maior número da serie D é: {maximo(list_D)}\n'
def main():
    print('Digite 4 séries de números contendo 4 numeros cada série para saber o maior numero de cada serie')
    while True:
        list_A = []
        list_B = []
        list_C = []
        list_D = []
        try:
            print('Números da série A')
            for i in range(4):
                num = int(input(f'Número {i + 1}: '))
                list_A.append(num)
            print('Números da série B')
            for i in range(4):
                num = int(input(f'Número {i + 1}: '))
                list_B.append(num)
            print('Números da série C')
            for i in range(4):
                num = int(input(f'Número {i + 1}: '))
                list_C.append(num)
            print('Números da série D')
            for i in range(4):
                num = int(input(f'Número {i + 1}: '))
                list_D.append(num)
            print(maior(list_A, list_B, list_C, list_D))
            break
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()