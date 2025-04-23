def notasAlunos():
    lista = []
    for i in range(50):
        num = float(input(f'Digite a {i + 1}° nota: '))
        lista.append(num)
    return lista

def alunos_aprovados(lista):
    indices_notas_aprovados = []
    for i in range(len(lista)):
        if lista[i] >= 6:
           indices_notas_aprovados.append(i)
    return indices_notas_aprovados 

def main():
    lista_notas = notasAlunos()
    indices_notas_aprovados = alunos_aprovados(lista_notas)
    print(f'A lista apenas com os índices dos alunos que tem nota maior ou igual a 6 é : \n{indices_notas_aprovados}')

if __name__ == "__main__":
    main()