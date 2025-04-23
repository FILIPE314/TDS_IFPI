# variável que nicializa a soma dos números
soma = 0
# Lê os 100 números inteiros
for numero in range(100):
    numero = int(input().strip())
    # adiciona o número à soma
    soma += numero
# Calcula o valor médio
media = soma / 100
# função (main) que inicia e termina o programa
def main():
    print(f"{media:.2f}")
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()