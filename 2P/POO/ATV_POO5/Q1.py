from random import *

def assentos_do_voo():
    assentos = []
    for c in range(5):
        assentos.append(randint(1, 100))
    return assentos
    
class Cartao_embarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data, hora, status_checkin = 'Não realizado', num_assento = 'Não selecionado'):
        self.nome_passageiro = nome_passageiro
        self.numero_voo = numero_voo
        self.codigo_reserva = codigo_reserva
        self.data = data
        self.hora = hora
        self.status_checkin = status_checkin
        self.num_assento = num_assento
    
    def realiza_checkin(self):
        self.status_checkin = 'Realizado'
        self.assentos = assentos_do_voo()
        self.num_assento = choice(self.assentos)

    def altera_assento(self, n_assento):
        if self.status_checkin == 'Realizado':
            if self.confere_assento_disponivel(n_assento):
                self.num_assento = n_assento
            else:
                return 'Este assento não está disponível'
        else:
            return 'Faça o check-in antes de trocar de assento'
    
    def confere_assento_disponivel(self, n_assento):
        return n_assento not in self.assentos

    def __str__(self):
        s1 = f'Nome passageiro: {self.nome_passageiro}\nNúmero do voo: {self.numero_voo}\nCógigo da reserva: {self.codigo_reserva}'
        s2 = f'\nData e hora de embarque: {self.data} às {self.hora} horas\nStatos do Check-in: {self.status_checkin}\nNúmero assento: {self.num_assento}'
        return s1+s2

def menu_cartao_embarque(nome_passageiro, numero_voo, cod_reserva, data, hora):
    meu_cartao_embarque = Cartao_embarque(nome_passageiro, numero_voo, cod_reserva, data, hora)
    print(meu_cartao_embarque)
    while True:
        opcao = int(input('''\nEscolha uma opção:
    1.Fazer check-in
    2.Alterar assento
    3.Terminar
    __'''))
    
        if opcao == 1:
            meu_cartao_embarque.realiza_checkin()
        elif opcao == 2:
            assento = int(input('Novo assento: '))
            meu_cartao_embarque.altera_assento(assento)
        elif opcao == 3:
            break
        return meu_cartao_embarque   
    
def main():
    cartao1 = menu_cartao_embarque('Luiz Filipe', 11, 'HFG476', '11/11/2024', '18:00')
    cartao2 = menu_cartao_embarque('Gabriel', 18, '84JFH4', '27/12/2024', '22:00')
    cartao3 = menu_cartao_embarque('Ane', 15, '998HDG', '7/09/2024', '15:00')
    
    print('Relatório de cartões de embarque\n')
    print(cartao1,'\n')
    print(cartao2,'\n')
    print(cartao3,'\n')

if __name__=='__main__':
    main()