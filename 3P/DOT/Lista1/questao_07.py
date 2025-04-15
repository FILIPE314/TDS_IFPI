# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.

def fatorial(num):
    valor = 1
    for i in range(num, 0, -1):
        valor *= i
    return valor

def main():
    while True:
        try:
            numero = int(input("\nDigite um número: "))
            if numero <= 0:
                print("\nERRO: O valor deve ser maior que 0!")
                main() # Para retornar ao início em caso de erro
            else:
                print(f"\nO fatorial de {numero} é: {fatorial(numero)}")
            break
        except:
            print("\nERRO: Entrada inválida, digite somente números inteiros!")            
if __name__=="__main__":
    main()
