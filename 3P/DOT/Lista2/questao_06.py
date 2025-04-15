# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.

# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 60
from random import randint
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 60)
        if x not in lista:
            lista.append(x)
    return lista

# Função que recebe uma lista de quantidade e outra de preço e gera outra lista com o faturamento de cada produto
def calcula_faturamento(lista_qtd, lista_valores):
    faturamentos = []
    for i in range(len(lista_qtd)):
        faturamentos.append(lista_qtd[i]*lista_valores[i])
    return faturamentos

# Função que recebe uma lista e um valor de média e retorna quantos valores da lista são menores do que a média 
def qtd_abaixo_da_media(lista, media):
    resultado = []
    for i in lista:
        if i < media:
            resultado.append(i)
    return len(resultado)

# Função que calcula a media dos elementos de uma lista
def media_lista(lista):
    return sum(lista)/len(lista)

def main():
    while True:
        quantidade_p = gera_lista(20)
        preco_p = [7, 5, 10.5, 8.7, 6.4, 9.34, 6.45, 9.6, 4.8, 3.5, 10, 6, 10.5, 8.7, 6.4, 5.8, 9.34, 6.45, 5.6, 4.8]
        if type(quantidade_p) != str and type(preco_p) != str:
            lista_faturamentos = calcula_faturamento(quantidade_p, preco_p)        
            media_faturamento = media_lista(lista_faturamentos)
            print(f'''\nFaturamento de cada produto em reais: {lista_faturamentos}
        \nFaturamento total: R$ {sum(lista_faturamentos):.2f}
        \nMédia dos faturamentos: R$ {media_faturamento:.2f}
        \nQuantidade de faturamentos abaixo da média: {qtd_abaixo_da_media(lista_faturamentos, media_faturamento)}''')
            break
        else:
            print("Entrada inválida! a lista deve ser de números, tente novamente!")
if __name__=="__main__":
    main()