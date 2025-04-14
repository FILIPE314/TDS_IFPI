# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

def somatorio(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return s

def  main():
    while True:
        try:
            numero = int(input("\nDigite um número: "))
            if numero > 0:    
                print(f"\nO somatório do número {numero} é: {somatorio(numero)}")
                break
            else:
                print("\nERRO: O número deve ser positivo e diferente de zero!")
        except:
            print("\nERRO: Entrada inválida, digite somente valores numéricos!")
if __name__=="__main__":
    main()