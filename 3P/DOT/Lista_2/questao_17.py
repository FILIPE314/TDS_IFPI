# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V aparece. Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.

#Função que confere quantas vezes o valor foi repetido na lista
def confere_repeticao(lista, valor):
    cont = 0
    for i in lista:
        if valor == i:
            cont += 1
    return cont

def main():
    lista_elementos = []
    cont = 0
    print("-----------Digite uma lista de 10 elementos.-----------")
    while cont < 10:
        cont += 1
        valor = input("--> ").strip()
        # Confere se o valor é vazio
        if not valor:
            cont -= 1
            print("\nERRO: Entrada inválida, não podem haver valores vazios!")  
        else:
            lista_elementos.append(valor)
    
    while True:
        v = input("\nDigite mais um valor: ").strip()
        # Confere se o valor é vazio
        if not valor:                  
            print("\nERRO: Entrada inválida, não podem haver valores vazios!")  
        else:
            print(f"\n{'='*10} {lista_elementos} {'='*10}")
            repeticao = confere_repeticao(lista_elementos, v)
            if repeticao == 0:
                print(f"\nO valor {v} NÃO ocorre nenhuma vez na lista!")
            else:
                print(f"\nNúmero de repetições de {v} na lista: {repeticao}")
            break
if __name__=="__main__":
    main()
