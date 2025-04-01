# =============================================================================================================================================================
# Questão 3
def celsius(graus):
    result = ((graus - 32) / 9) * 5
    return f'Temperatura: {result:.2f}C°'
def main():
    while True:
        try:
            graus = float(input('\nDigite uma temperatura em Fahrenheith para saber seu valor em graus Celsisu:\num'))
            print(celsius(graus))
            break
        except:
            print('Ops... Algo deu errado, digite um valor válido!')
if __name__ == '__main__':
    main()