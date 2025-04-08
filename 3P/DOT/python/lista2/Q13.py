# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o 
# lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de 
# cada face.
from random import randint
def dado_viciado(lados):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    for i in lados:
        if lados[i] == 1:
            num1 += 1
        if lados[i] == 2:
            num2 += 1
        if lados[i] == 3:
            num3 += 1
        if lados[i] == 4:
            num4 += 1
        if lados[i] == 5:
            num5 += 1
        if lados[i] == 6:
            num6 += 1
    return f'\nO lado do número 1 caiu {num1} vezes\n' + \
           f'\nO lado do número 2 caiu {num2} vezes\n' + \
           f'\nO lado do número 3 caiu {num3} vezes\n' + \
           f'\nO lado do número 4 caiu {num4} vezes\n' + \
           f'\nO lado do número 5 caiu {num5} vezes\n' + \
           f'\nO lado do número 6 caiu {num6} vezes'
def main():
    lados = []
    while True:
        try:
            vezes_lancar = int(input(f'Digite quantas vezes lançar um dado para saber se ele esta viciado: '))
            for i in range(vezes_lancar):
                lados.append(randint(1, 6))
            print(dado_viciado(lados))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()