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

def aniversario_cidades(dia, mes, cidades):
    lista_cidades_encontradas = []
    for cidade in cidades:
        if cidade[3] == dia and cidade[4] == mes:
            lista_cidades_encontradas.append(f'{cidade[2]}({cidade[0]})')          
    return lista_cidades_encontradas

def mes_por_extenso(mes):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    return meses[mes - 1] # ex: se mes 1, o indice será 1 - 1 = 0. 

def main():
    cidades = carrega_cidades() # tem a lista de todas as cidades com as informações

    dia = int(input())
    mes = int(input())

    encontrados = aniversario_cidades(dia, mes, cidades)

    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes_por_extenso(mes).upper()}:')
    for encontrado in encontrados:
        print(encontrado)

if __name__ == "__main__":
    main()