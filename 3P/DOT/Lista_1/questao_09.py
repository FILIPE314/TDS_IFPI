# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.

def calcula_soma(n1, n2):
    soma = 0
    for i in range(n1, n2):
        soma += i
    return soma

def main():
    while True:
        try:
            n1 = int(input("\nDigite o primeiro número: "))
            n2 = int(input("\nDigite o segundo número: "))
            
            if n1 >= n2:
                print("\nERRO: O primeiro número deve ser menor do que o segundo e os dois números não pode ser iguais!")
            else:
                print(f"\nA soma do intervalo entre {n1} e {n2} é: {calcula_soma(n1, n2)}")
                break
        except:
            print("\nERRO: Entrada inválida, digite apenas números!")    
if __name__=="__main__":
    main()
