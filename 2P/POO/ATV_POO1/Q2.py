import random
class ppt:
    usuario = None
    pc = None
    pontuacao = 0
    pontuacao_pc = 0

    def jogo(self):
        if self.usuario == self.pc:
            return 'EMPATE!'
        elif self.usuario == 'papel' and self.pc == 'pedra' or self.usuario == 'tesoura' and self.pc == 'papel' or self.usuario == 'pedra' and self.pc == 'tesoura':
            self.pontuacao += 1
            return 'Você venceu, parabéns!!!'
        elif self.usuario == 'pedra' and self.pc == 'papel' or self.usuario == 'papel' and self.pc == 'tesoura' or self.usuario == 'tesoura' and self.pc == 'pedra':
            self.pontuacao_pc += 1
            return 'Você perdeu :('
        
def main():
    print('Bem vindo ao jogo de pedra, papel e tesoura!')
    result = ppt()
    while True:
        result.pc = random.choice(['pedra', 'papel', 'tesoura'])
        result.usuario = input('Escolha entre PEDRA, PAPEL ou TESOURA. Se quiser encerrar o jogo é so digitar (x):').lower()
        if result.usuario == 'x':
            print('Encerrando o jogo...')
            break
        if result.usuario == 'tesoura' or result.usuario == 'papel' or result.usuario == 'pedra':
            print(result.jogo())
        else:
            print('Tente novamente...')
            return main()
        print('O pc escolheu:', result.pc)
    print('Seus pontos', result.pontuacao)
    print('Pontos do pc', result.pontuacao_pc)
if __name__ == '__main__':
    main()