# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
def fatorar(num):
    lita_fatoracao = []
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    cont = 0
    while num != 1:
        if num % primos[cont] == 0:
            num /= primos[cont]
            lita_fatoracao.append(primos[cont])
        else:
            cont += 1
    return lita_fatoracao 

def numero_divisores(num):
    lista_fatores = fatorar(num) 
    lista = []
    cont = 0
    x = 0
    for i in lista_fatores:
        if i == lista_fatores[x]:
            cont += 1
        else:
            x += 1
            lista.append(cont)
            cont = 0       
        
    return lista
            
def main():
    while True:
        try:
            numero = int(input("Digite um número: "))
            print(f"{numero_divisores(numero)}\n")
            break

        except:
            print("\nERRO: Entrada inválida, digite somente valores numéricos!")

if __name__=="__main__":
    main()