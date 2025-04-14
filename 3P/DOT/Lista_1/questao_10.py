# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada quatro números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b, c, d. Para cada série lida imprime o maior dos quatro números usando a função
# Max.
# c) Retorne o maior das quatro séries lidas

def max(n1, n2, n3, n4):
    lista = [n1, n2, n3, n4]
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior    

def main():
    lista_series = []
    i = 0
    while i < 4:
        i+= 1
        try:
            n1 = int(input("\nDigite o primeiro número: "))
            n2 = int(input("\nDigite o segundo número: "))
            n3 = int(input("\nDigite o terceiro número: "))
            n4 = int(input("\nDigite o quarto número: "))
            
            maior = max(n1, n2, n3, n4)
            print(f"O maior entre {n1}, {n2}, {n3} e {n4} é: {maior}")
            lista_series.append(maior)
        except:
            i -= 1
            print("\nERRO: Entrada inválida, digite apenas números!")

    print(f"O maior da lista das quatro séries {lista_series} é: {max(lista_series[0], lista_series[1], lista_series[2], lista_series[3])}")
if __name__=="__main__":
    main()
