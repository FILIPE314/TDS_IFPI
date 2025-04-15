# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.

# Função que confere se um número está presente na lista, retorna um valor booleano
def verifica_num_lista(lista, num):
    if num in lista:
        return True
    else:
        return False

def main():
    while True:
        try:
            lista = [1,5,9,7,3,10,54,20,6.5,26]
            num = float(input("\nDigite um valor para conferir se está na lista: "))
            resposta = verifica_num_lista(lista, num)
            if type(lista) != str:
                if resposta == True:
                    print(f"\nO número {num} ESTÁ presente na lista: {lista}")
                else:
                    print(f"\nO número {num} NÃO está na lista: {lista}")
                break
        except:
            print("\nEntrada inválida! a lista deve ser de números, tente novamente!")
if __name__=="__main__":
    main()