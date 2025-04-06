# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre: 
# a) O maior elemento da lista e em que posição esse elemento se encontra; 
# b)    O menor elemento da lista e em que posição esse elemento se encontra.
def maior_position(list):
    maior = list[0]
    position = -1
    for i in list:
        if i > maior:
            maior = i
    for i in range(len(list)):
        if list[i] == maior:
            position = i
            break
    return f'\nO maior número é {maior} e a posição dele na lista é {position}'
def menor_position(list):
    menor = list[0]
    position = -1
    for i in list:
        if i < menor:
            menor = i
    for i in range(len(list)):
        if list[i] == menor:
            position = i
            break
    return f'\nO maior número é {menor} e a posição dele na lista é {position}'
def main():
    lista = []
    while True:
        try:
            for i in range(1, 15):
                num = int(input('\nDigite um número para adicioná-lo a uma lista de 15 números: '))
                lista.append(num)
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
    print(maior_position(lista))
    print(menor_position(lista))
if __name__ == '__main__':
    main()