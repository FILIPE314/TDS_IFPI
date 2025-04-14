def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def populacao_maior(populacao, cidades):
    lista_cidades_encontradas = []
    for cidade in cidades:
        if cidade[5] > populacao:
            # IBGE: 292740 - Salvador(BA) - POPULAÇÃO: 2892625
            lista_cidades_encontradas.append(f'IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}')          
    return lista_cidades_encontradas

def main():
    cidades = carrega_cidades() # tem a lista de todas as cidades com as informações

    populacao = int(input())

    encontrados = populacao_maior(populacao, cidades)

    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    for encontrado in encontrados:
        print(encontrado)

if __name__ == "__main__":
    main()