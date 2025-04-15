# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face. 

# faer uma função para gerar os números do dados de forma aleatória
from random import randint

def main():
    while True:
        try:
            numero_lancamentos = int(input("\nDigite quantas vezes desejar lançar o dado: "))
            # Tratar valor <= 0
            if numero_lancamentos > 0:
                faces = [0,0,0,0,0,0]
                instancias = []
                for i in range(numero_lancamentos):
                    face = randint(1, 6)
                    # Incrementa o valor 1 à posição correspondente a face que caiu
                    faces[face-1] += 1
                    instancias.append(face)
                    
                print(f"\nFaces que cairam após cada lançamento: {instancias}")
                print(f"\n{'='*5} Número de ocorrências de cada face {'='*5}")
                for i in range(6):
                    print(f"Face {i+1}: {faces[i]}")
                break
            else:
                print("\nERRO: O número de lançamentos não pode ser menor ou igual a zero. Tente novamente!")             
        except:
            print("\nERRO: Entrada inválida, digite apenas números. Tente novamente!")          
    
if __name__=="__main__":
    main()