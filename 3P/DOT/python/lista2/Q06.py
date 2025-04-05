# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um 
# programa  que  calcule  e  exiba  o faturamento que  é igual a  quantidade  x preço. Calcule  e exiba 
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos 
# e quantos faturamentos estão abaixo da média.
def faturamento(quantidade, precos):
    media = 0
    abaixo_media = 0
    abaixo_media_detalhado = []
    soma_faturamentos = 0
    todos_faturamentos = []
    for i in range(20):
        result = quantidade[i] * precos[i]
        todos_faturamentos.append(result)
        soma_faturamentos += result
    media = soma_faturamentos / 20
    for i in range(len(todos_faturamentos)):
        if todos_faturamentos[i] < media:
            abaixo_media += 1
            abaixo_media_detalhado.append(todos_faturamentos[i])
    return  f'\nCada faturamento: {todos_faturamentos}\n' + \
            f'\nFaturamento total: {soma_faturamentos:.2f}\n' + \
            f'\nMédia de faturamentos: {media}\n' + \
            f'\nFaturamentos abaixo da média: {abaixo_media}\n' + \
            f'\nTodos abaixo da média detalhadamente: {abaixo_media_detalhado}\n'
def main():
    quantidade = list(range(11, 31))
    precos = list(range(21, 41))
    while True:
        try:
            print(faturamento(quantidade, precos))
            # print(f'{quantidade}\n {precos}')
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
            break
if __name__ == '__main__':
    main()