def ler_dados(n):
    lista_nomes = []
    lista_alturas = []
    for i in range(n):
        nome = input(f'Digite o {i+1}° nome: ').strip()
        altura = float(input(f'Digite a altura do {nome.upper()}: '))
        lista_nomes.append(nome)
        lista_alturas.append(altura)
    return lista_nomes, lista_alturas

def media_altura(lista):
    media = sum(lista)/len(lista)
    return media 

def main():
    qtdJogadores = 12
    lista_nomes, lista_alturas = ler_dados(qtdJogadores)
    media = media_altura(lista_alturas)

    maiorAltura = max(lista_alturas)
    index_maiorAltura = lista_alturas.index(maiorAltura)
    nomeMaisAlto = lista_nomes[index_maiorAltura]

    print('JOGADOR MAIS ALTO DO TIME')
    print(nomeMaisAlto) # nome 
    print(f'{maiorAltura:.2f}') # maior altura

    print('ALTURA MÉDIA DO TIME')
    print(f'{media:.2f}')    

    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for i in range(qtdJogadores):
        if lista_alturas[i] >= media:           
            print(lista_nomes[i])
            print(f'{lista_alturas[i]:.2f}')


if __name__ == '__main__':
    main()