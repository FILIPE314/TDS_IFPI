def main():
    valorFinal = 0
    while True:
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        pedido = str(input().strip()).upper()[0]
        if pedido == 'H':
            valorFinal = valorFinal + 5.50
        elif pedido == 'C':
            valorFinal = valorFinal + 6.80
        elif pedido == 'M':
            valorFinal = valorFinal + 4.50
        elif pedido == 'A':
            valorFinal = valorFinal + 7
        elif pedido == 'Q':
            valorFinal = valorFinal + 4
        elif pedido == 'X':
            break
        else:
            print('Código inválido.')
    print(f'{valorFinal:.2f}')

if __name__ == '__main__':
    main()