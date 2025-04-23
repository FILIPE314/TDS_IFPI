# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas. 

# Função que gera uma lista aleatória de respostas de "A" a "E", com tamanho determinado ao chamar a função, retornando ao final a lista criada
import random
def gera_respostas(num_questoes):
    alternativas = ["A","B","C","D","E"]
    lista = []
    for i in range(num_questoes):
        lista.append(random.choice(alternativas))
    return lista
    
def main():
    while True:
        try:
            num_alunos = int(input("\nDigite o número de alunos da turma: "))            
            if num_alunos > 0:
                gabarito = gera_respostas(30)                
                respostas_alunos = []
                acertos = []
                # Faz um script para cada aluno da lista
                for c in range(num_alunos):
                    aluno = gera_respostas(30)
                    aluno_acertos = 0
                    # Compara cada resposta do aluno com o gabarito 
                    for i in range(len(aluno)):
                        if aluno[i] == gabarito[i]:
                            aluno_acertos += 1
                    respostas_alunos.append(aluno)
                    acertos.append(aluno_acertos)
                    
                print(f"\nGabarito da prova: {gabarito}\n\n{'='*10} RESULTADO DA PROVA! {'='*10}")                
                n = 0
                for i in range(len(respostas_alunos)):
                    print(f"Número de acertos aluno {n+1}: {acertos[n]}")
                    n += 1
                break
            else:
                print("\nERRO: O número de alunos não pode ser menor ou igual a zero. Tente novamente!")
        except:
            print("\nERRO: Entrada inválida, digite apenas números. Tente novamente!")    
if __name__=="__main__":
    main()
    
