# função(condicional) que verifica se é masculino ou feminino
def sexo(masculino_ou_feminino,altura):
    # condicional(verdadeira) que verifica o resultado
    if masculino_ou_feminino == 1:
        # retorna o resutado caso seja esssa opção
        return (72.7 * altura) - 58
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return (62.1 * altura) - 44.7
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    altura = float(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    masculino_ou_feminino = int(input().strip())
    # Imprime uma informação na tela e acionando a função
    print(f'{sexo(masculino_ou_feminino,altura):.2f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()