# função que separa a data e retorna o valor se é verdadeira ou falsa
def separar_data (data):
    aa = data % 10000
    data //= 10000
    mm = data % 100
    data //= 100
    dd = data
    if mm == 2:
        if (aa % 4 == 0 and aa % 100 != 0) or (aa % 400 == 0):
            return aa > 0 and 12 >= mm > 0 and 29 >= dd > 0
        else:
            return aa > 0 and 13 > mm > 0 and 28 >= dd > 0        
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        return aa > 0 and 12 >= mm > 0 and 30 >= dd > 0
    else:
        return aa > 0 and 12 >= mm > 0 and 31 >= dd >0
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    data = int(input())
    # acionando a função e imprimindo
    print(separar_data(data))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()