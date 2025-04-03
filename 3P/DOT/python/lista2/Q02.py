# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade 
# de números negativos e a soma dos números positivos dessa lista.
def num_negative(list):
    result = 0
    for i in list:
        if i < 0:
            result += 1
    return f'\nNúmeros negativos: {result}'
def num_positive(list):
    result = 0
    for i in list:
        if i > 0:
            result += i
    return f'\nSoma dos números positivos: {result}'
def main():
    lista = []
    i =  0
    print('Digite 10 números reais para saber a quantidade de números negativos e a soma dos números positivos')
    while i < 10:
        i += 1
        try:
            num = int(input(f'\nDigite o número {i}: '))
            lista.append(num)
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
            break
    print(num_negative(lista))
    print(num_positive(lista))
if __name__ == '__main__':
    main()