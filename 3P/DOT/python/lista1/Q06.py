# =============================================================================================================================================================
# Questão 6
def a_p(lado, m_lado):
    if lado == 3:
        tri = m_lado * 3
        return f'TRIÂNGULO {tri:.0f}'
    if lado == 4:
        qua = m_lado ** 2
        return f'QUADRADO {qua:.0f}'
    if lado == 5:
        return f'PENTÁGONO'
    else:
        return f'Ops... Valor inválido!'
def main():
    while True:
        try:
            lado = int(input('Digite a quantidade de lados: '))
            m_lado = float(input('Digite o tamanho em centímetros de um lado: '))
            if lado > 0 and m_lado > 0:
                print(a_p(lado, m_lado))
                break
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()