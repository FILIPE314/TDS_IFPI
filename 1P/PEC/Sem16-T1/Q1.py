def ler_matriz(n):
    matriz = []
    print(f"Digite os {n*n} elementos da matriz:")
    for i in range(n):
        linha = []
        for j in range(n):
            valor = float(input(f"Elemento [{i+1}, {j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def posicao_maior_menor(matriz):
    n = len(matriz)
    maior_valor = matriz[0][0]
    menor_valor = matriz[0][0]
    pos_maior = (0, 0)
    pos_menor = (0, 0)
    
    for i in range(n):
        for j in range(n):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                pos_maior = (i, j)
            if matriz[i][j] < menor_valor:
                menor_valor = matriz[i][j]
                pos_menor = (i, j)
    
    return pos_maior, pos_menor

def main():
    n = int(input("Informe a ordem da matriz (n): "))
    matriz = ler_matriz(n)
    
    pos_maior, pos_menor = posicao_maior_menor(matriz)
    
    print(f"Posição do maior elemento: {pos_maior}")
    print(f"Posição do menor elemento: {pos_menor}")

if __name__ == "__main__":
    main()