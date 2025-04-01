# =============================================================================================================================================================
# Questão 5
def peso_ideal(altura, sexo):
    if sexo == 1:
        pi = (62.1 * altura) - 44.7
        return f'Seu peso deve ser: {pi:.2f}'
    else:
        pi = (72.7 * altura) - 58
        return f'Seu peso deve ser: {pi:.2f}'
def main():
    while True:
        print('Coloque seu peso e sua altura e o seu sexo para saber seu peso ideal')
        try:
            altura = float(input('Sua altura: '))
            sexo = int(input('Seu sexo - (sendo 1 para feminino e 2 para masculino): '))
            if sexo == 1 or sexo == 2 and altura > 0:
                print(peso_ideal(altura, sexo))
                break
            else:
                print('Ops... Digite um valor válido!')
        except:
            print('Ops... Digite um valor válido!')
if __name__ == '__main__':
    main()