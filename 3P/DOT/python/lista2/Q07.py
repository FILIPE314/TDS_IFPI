# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um 
# outro valor dado pertence ou não à lista.
def verifica(lista, valor_aribuido):
    for i in range(len(lista)):
        if valor_aribuido == lista[i]:
            return f'\nEsse valor já pertence a lista\n'
    return f'\nEsse valor não pertence a essa lista\n'
def main():
    lista = list(range(50, 61))
    while True:
        try:
            valor_aribuido = int(input('Digite um valor para saber se ele esta atribuido a uma lista: '))
            print(verifica(lista, valor_aribuido))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()