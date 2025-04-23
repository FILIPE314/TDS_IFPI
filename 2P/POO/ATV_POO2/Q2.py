class bicicleta:
    velocidade_atual = 0
    altura_cela = 0
    calibragem_pneus = 0

    def __init__(self, velocidade):
        self.velocidade_atual = velocidade
    
    def regular(self):
        if self.velocidade_atual == 0:
            self.altura_cela = int(input('Digite uma altura da cela caso queira alterar. Se não quiser digite (77).'))
            self.calibragem_pneus = int(input('Digite uma calibragem para os pneus caso queira alterar. Se não quiser digite (77).'))
            if 25 >= self.altura_cela >= 0 and 25 > self.calibragem_pneus == 0:
                return 'Altura da cela:' + f'{self.altura_cela}' + ' Calibragem dos pneus:' + f'{self.calibragem_pneus}'
            elif self.calibragem_pneus > 25:
                return 'Valor errado ou passou dos limites.'
            if 25 >= self.altura_cela >= 0 and 25 > self.calibragem_pneus > 0:
                return 'Altura da cela:' + f'{self.altura_cela}' + ' Calibragem dos pneus:' + f'{self.calibragem_pneus}'
            elif self.altura_cela > 25:
                return 'Valor errado ou passou dos limites.'
            elif self.altura_cela == 77 and self.calibragem_pneus == 77:
                return 'Você não alterou nada'
        if 100 > self.velocidade_atual > 0:
            self.velocidade_atual = int(input('Altere a velocidade atual(Enquanto estiver em movimeno não poderá alterar a altura da cela nem a calibragem dos pneus.)'))
            self.regular()
        else:
            return 'Valor errado ou passou dos limites.'
        
def main():
    while True:
        bike = bicicleta(velocidade = int(input('Altere a velocidade, caso queira continuar parado digite (0).')))
        print(bike.regular())
        print(f'Velocidade atual:{bike.velocidade_atual}')
if __name__ == '__main__':
    main()