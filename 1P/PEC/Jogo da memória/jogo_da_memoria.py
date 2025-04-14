
def remover_acentos(texto):
    # Importa a função normalize do módulo unicodedata para lidar com caracteres Unicode
    from unicodedata import normalize
    # Retorna o texto sem acentos
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
# Função que separa a data por meio de cálculos
def separar_data(dma):
    # Extrai o ano
    a = dma % 10000
    dma //= 10000
    # Extrai o mês
    m = dma % 100 
    dma //= 100
    # O que sobrar será o dia
    d = dma
    return d, m, a
# Função(condicional) que determina o signo com base no dia e no mês
def signo(dia, mes):
    # complementar da função
    if mes == 3:
        # retorna o valor caso seja essa a opção
        return 'Peixes' if dia < 21 else 'Áries'
    # complementar da função
    if mes == 4:
        # retorna o valor caso seja essa a opção
        return 'Áries' if dia < 20 else 'Touro'
    # complementar da função
    if mes == 5:
        # retorna o valor caso seja essa a opção
        return 'Touro' if dia < 21 else 'Gêmeos'
    # complementar da função
    if mes == 6:
        # retorna o valor caso seja essa a opção
        return 'Gêmeos' if dia < 22 else 'Câncer'
    # complementar da função
    if mes == 7:
        # retorna o valor caso seja essa a opção
        return 'Câncer' if dia < 23 else 'Leão'
    # complementar da função
    if mes == 8:
        # retorna o valor caso seja essa a opção
        return 'Leão' if dia < 23 else 'Virgem'
    # complementar da função
    if mes == 9:
        # retorna o valor caso seja essa a opção
        return 'Virgem' if dia < 23 else 'Libra'
    # complementar da função
    if mes == 10:
        # retorna o valor caso seja essa a opção
        return 'Libra' if dia < 23 else 'Escorpião'
    # complementar da função
    if mes == 11:
        # retorna o valor caso seja essa a opção
     return 'Escorpião' if dia < 22 else 'Sagitário'
    # complementar da função
    if mes == 12:
        # retorna o valor caso seja essa a opção
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    # complementar da função
    if mes == 1:
        # retorna o valor caso seja essa a opção
        return 'Capricórnio' if dia < 20 else 'Aquário'
    # complementar da função
    if mes == 2:
        # retorna o valor caso seja essa a opção
        return 'Aquário' if dia < 19 else 'Peixes'
# função para a resposta final
def horoscopo(signo_desejado): 
    # Importa o módulo urllib.request para fazer requisições HTTP
    import urllib.request
    # Formata o nome do signo para usar na URL
    signo_formatado = remover_acentos(signo_desejado).lower()
    # URL do site do horóscopo
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado
    # Cria uma requisição para acessar a página do signo desejado
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'})
    # Abre a página do signo desejado
    resposta = urllib.request.urlopen(requisicao)
    # Lê o conteúdo da página
    pagina = resposta.read().decode('utf-8')
    # Define os marcadores para encontrar a previsão do horóscopo na página
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'
    # Encontra a posição inicial da previsão do horóscopo
    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    # Encontra a posição final da previsão do horóscopo
    final = pagina.find(marcador_final, inicio)
    # Retorna o signo e a previsão do horóscopo
    return signo_desejado + ': ' + pagina [inicio: final]
def main():
    #Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))
    #Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes) 
    horoscopo_de_hoje = horoscopo (meu_signo)
    #Saída de dados print(horoscopo_de_hoje)
    print(horoscopo_de_hoje)
if __name__ == '__main__':
    main()