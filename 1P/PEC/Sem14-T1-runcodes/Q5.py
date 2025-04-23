def ler_dados(n):
    lista_nomes = []
    lista_idades = []
    lista_alturas = []
    for i in range(n):
        nome = input().strip()
        idade = int(input())
        altura = float(input())
        lista_nomes.append(nome)
        lista_idades.append(idade)
        lista_alturas.append(altura)
    return lista_nomes, lista_idades, lista_alturas

def media_altura(lista):
    media = sum(lista)/len(lista)
    return media

def main():
    qntdAlunos = 30
    lista_nomes, lista_idade, lista_altura = ler_dados(qntdAlunos)
    media = media_altura(lista_altura)
    media = round(media, 2)
    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    for i in range(qntdAlunos):
        if lista_idade[i] > 13 and lista_altura[i] < media:
            print(lista_nomes[i])

if __name__ == '__main__':
    main()