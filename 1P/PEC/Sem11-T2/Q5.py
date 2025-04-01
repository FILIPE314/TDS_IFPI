def main():
    while True:
        nota = float(input('Insira uma nota: ').strip())
        if nota > 10 or nota < 0: 
            print('Nota inválida.')
        else:
            break
    if nota >= 8.5:
        print('Conceito A')
        print('Parabéns!')
    elif nota >= 7:
        print('Conceito B')
        print('Parabéns!')
    elif nota >= 5:
        print('Conceito C')
        print('Estude mais!')
    elif nota >= 4:
        print('Conceito D')
        print('Estude mais!')
    elif nota >= 0:
        print('Conceito E')
        print('Estude mais!')

if __name__ == '__main__':
    main()