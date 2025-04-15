# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

def qtd_negativos(lista):
    qtd = 0
    for i in lista:
        if i < 0:
            qtd +=1
    return qtd
def soma_positivos(lista):
    soma = 0
    for i in lista:
        if i >= 0:
            soma += i
    return soma

def main():
    while True:
        try:
            lista_numeros = []
            print(f"{'='*20} Digite 10 números reais {'='*20}")
            for i in range(10):        
                num = float(input("--> "))
                lista_numeros.append(num)

            qtd_num_negativos = qtd_negativos(lista_numeros)
            soma_num_positivos = soma_positivos(lista_numeros)

            print(f"\nLista: {lista_numeros}\nQuantidade de números negativos: {qtd_num_negativos}\nSoma dos números positivos: {soma_num_positivos}")
            break
        except:
            print("Entrada inválida! Digite apenas números reais, tente novamente.")
if __name__=="__main__":
    main()


