# variável que inicializa a sequência com o primeiro número
sequencia = ""
# gera a sequência de números de 10 a 1000, incrementando de 10 em 10
for numero in range(10, 1001, 10):
    # adiciona o número à sequência
    sequencia += str(numero) + ", "
# remove o espaço e a vírgula extra no final da sequência
sequencia = sequencia.strip(", ")
# adiciona o ponto final
sequencia += "."
# função (main) que inicia e termina o programa
def main():
    # exibe a sequência
    print(sequencia)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()