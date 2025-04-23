def main():
    dataNascimento = input('Digite sua data de nascimento, no formato ddmmaaaa: ')
    i = 0
    numeroSorte = 0

    while i < len(dataNascimento): 
        numeroSorte += int(dataNascimento[i])
        i += 1
    print(f'Seu número da sorte é: {numeroSorte}')

if __name__ == '__main__':
    main()