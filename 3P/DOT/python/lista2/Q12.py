# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A 
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. 
# Para isso são dados:  o cartão gabarito;  o número de alunos da turma;  o cartão de respostas 
# para cada aluno, contendo o seu número e suas respostas.
from random import randint
def num_acertos(gabarito, cartao_aluno):
    acerto = 0
    for i in range(len(gabarito)):
        if gabarito[i] == cartao_aluno[1][i]:
            acerto += 1
    return f'O aluno de número {cartao_aluno[0]}, acertou {acerto} questões'
def main():
    numero_de_alunos = 20
    for i in range(numero_de_alunos):
        alternativas = ['a', 'b', 'c', 'd', 'e']
        gabarito = ['a', 'a', 'b', 'e', 'd', 'b', 'c', 'd', 'e', 'a', 'e', 'a', 'b', 'e', 'a', 'e', 'b', 'a', 'd', 'e', 'b', 'b', 'c', 'd', 'e', 'c', 'a', 'e', 'b']
        resposta = []
        while True:
            try:
                cartao_aluno = [randint(100, 999), resposta]
                for i in range(1, 31):
                    a = randint(0, 4)
                    resposta.append(alternativas[a])
                print(num_acertos(gabarito, cartao_aluno))
                break
            except:
                print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()