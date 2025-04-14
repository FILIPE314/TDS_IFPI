# função(aninhada) que lê um número de 999 a 99 e o digita por extenso
def cdu1(num):
    if 99 < num < 1000:
        x = num // 100
        if x == 1:
            return 'uma centena,'
        elif x == 2:
            return 'duas centenas,'
        elif x == 3:
            return 'três centenas,'
        elif x == 4:
            return 'quatro centenas,'
        elif x == 5:
            return 'cinco centenas,'
        elif x == 6:
            return 'seis centenas,'
        elif x == 7:
            return 'sete centenas,'
        elif x == 8:
            return 'oito centenas,'
        elif x == 9:
            return 'nove centenas,'
    else:
        return ''
# função(aninhada) que lê um número de 999 a 9 e o digita por extenso
def cdu2(num):
    if 9 < num < 1000:
        x = num // 100
        y = num - (100 * x)
        z = y // 10
        if z == 1:
            return 'uma dezena'
        elif z == 2:
            return 'duas dezenas'
        elif z == 3:
            return 'três dezenas'
        elif z == 4:
            return 'quatro dezenas'
        elif z == 5:
            return 'cinco dezenas'
        elif z == 6:
            return 'seis dezenas'
        elif z == 7:
            return 'sete dezenas'
        elif z == 8:
            return 'oito dezenas'
        elif z == 9:
            return 'nove dezenas'
        else:
            return ''
# função(aninhada) que lê um número de 999 a 0 e o digita por extenso
def cdu3(num):
    if 0 < num < 1000:
        x = num // 100
        y = num - (100 * x)
        z = y // 10
        a = y - (10 * z)
        b = a // 1
        if b == 1:
            return 'e uma unidade'
        elif b == 2:
            return 'e duas unidades'
        elif b == 3:
            return 'e três unidades'
        elif b == 4:
            return 'e quatro unidades'
        elif b == 5:
            return 'e cinco unidades'
        elif b == 6:
            return 'e seis unidades'
        elif b == 7:
            return 'e sete unidades'
        elif b == 8:
            return 'e oito unidades'
        elif b == 9:
            return 'e nove unidades'
        else:
            return ''
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num = int(input())
    # acionando a função
    print(cdu1(num),cdu2(num),cdu3(num))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()