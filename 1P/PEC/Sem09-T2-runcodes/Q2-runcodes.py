# função(aninhada) que lê um número de 999 a 99 e o digita por extenso
def cdu1(num):
    if 99 < num < 1000:
        x = num // 100
        if x == 1:
            return 'uma centena'
        elif x == 2:
            return 'duas centenas'
        elif x == 3:
            return 'três centenas'
        elif x == 4:
            return 'quatro centenas'
        elif x == 5:
            return 'cinco centenas'
        elif x == 6:
            return 'seis centenas'
        elif x == 7:
            return 'sete centenas'
        elif x == 8:
            return 'oito centenas'
        elif x == 9:
            return 'nove centenas'
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
            return 'uma unidade'
        elif b == 2:
            return 'duas unidades'
        elif b == 3:
            return 'três unidades'
        elif b == 4:
            return 'quatro unidades'
        elif b == 5:
            return 'cinco unidades'
        elif b == 6:
            return 'seis unidades'
        elif b == 7:
            return 'sete unidades'
        elif b == 8:
            return 'oito unidades'
        elif b == 9:
            return 'nove unidades'
        else:
            return ''
# função para responder de um jeito diferente dependendo do redultado das outras funções
def modif(centena,dezena,unidade,num):
    if num == 1:
        print('uma unidade'+'.')
    elif num == 2:
        print('duas unidades'+'.')
    elif num == 3:
        print('três unidades'+'.')
    elif num == 4:
        print('quatro unidades'+'.')
    elif num == 5:
        print('cinco unidades'+'.')
    elif num == 6:
        print('seis unidades'+'.')
    elif num == 7:
        print('sete unidades'+'.')
    elif num == 8:
        print('oito unidades'+'.')
    elif num == 9:
        print('nove unidades'+'.')
    elif centena == '' and dezena == '':
        print(unidade+'.')
    elif centena == '' and unidade == '':
        print(dezena+'.')
    elif dezena == '' and unidade == '':
        print(centena+'.')
    elif centena == '':
        print(dezena+' e '+unidade+'.')
    elif dezena == '':
        print(centena+' e '+unidade+'.')
    elif unidade == '':
        print(centena+' e '+dezena+'.')
    else:
        print(centena+', '+dezena+' e '+unidade+'.')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num = int(input().strip())
    # variável que armazena dados
    centena = cdu1(num)
    # variável que armazena dados
    dezena = cdu2(num)
    # variável que armazena dados
    unidade = cdu3(num)
    # acionando a função
    modif(centena,dezena,unidade,num)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()