# Utilizando o processo de abstração, implemente uma classe em Python que represente um cartão de embarque de voo. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis.
from datetime import datetime
import random

class CartaoEmbarque:
    # Método construtor/inicializador:
    def __init__(self, nome, voo, localizador, data_hora_emb):
        self.nome = nome
        self.voo = voo
        self.localizador = localizador
        self.data_hora_emb = data_hora_emb
           
    # Alterar o status e associar um assento (aleatório) disponível ao passageiro.    
    def realizar_check_in (self, status=False, assento=None):
        self.status = status
        self.assento = assento
        assentos_disponiveis = ('5B','5D','19A', '19B', '19F', '32C')
        
        check_in = input(f'{self.nome}, deseja fazer o check-in? S/N ').strip().upper()
        
        #Se o passageiro não quiser fazer o check-in, imprimir a mensagem de "check-in não realizado" e as informações do cartão de embarque. 
        if check_in == 'N':
            self.status = 'Check-in não realizado.'
            return self
        #Se o passageiro quiser fazer o check-in, oferecer a opção de escolher o assento.
        elif check_in == 'S':
            escolher_assento = input('Deseja escolher o assento? S/N ').strip().upper()
            #Se o passageiro não quiser escolher o assento, definir uma opção aleatoriamente, alterar o status para "Check-in realizado", e imprimir as informações do cartão de embarque
            if escolher_assento == 'N':
                self.status = 'Check-in realizado com sucesso!'
                self.assento = random.choice(assentos_disponiveis)
                return f'{self.status}\n{self}Assento:{self.assento}'
            #Se o passageiro quiser escolher o assento, imprimir os assentos disponíveis, alterar o assento para a opção desejada, remover o assento da lista de assentos disponíveis, alterar o status para "Check-in realizado", e imprimir as informações do cartão de embarque
            elif escolher_assento == 'S':
                self.status = 'Check-in realizado com sucesso!'
                print (f'Assentos Disóníveis: {assentos_disponiveis}')
                self.assento = input('Informe o assento desejado: ').strip().upper()
                #remover o assento escolhido da lista
                return f'{self.status}\n{self}Assento:{self.assento}'
            else:
                raise ValueError ('Opção inválida.')
        else:
            raise ValueError ('Opção inválida.')
        
        # Validações para garantir que o check-in só possa ser feito uma vez.
        pass
    def alterarr_assento (self, status, assento):
        
        # alterar o assento (apenas se o check-in já tiver sido realizado).
        # Validações para garantir que assentos indisponíveis não sejam atribuídos.
        pass
    def validar_reserva (self, reserva):
        # o código da reserva deve ter 6 caracteres alfanuméricos
        pass
    def validar_hora (self, hora):
        # a hora do embarque não pode ser retroativa em relação ao momento de execução do código.
        pass
    def __str__(self) -> str:
        return (f'Passageiro: {self.nome}\n'
                f'Vôo: {self.voo}\n'
                f'Localizador: {self.localizador}\n' 
                f'Embarque: {self.data_hora_emb}\n'
                # f'Status: {self.status}\n'
                # f'Assento: {self.assento}\n'
                )
    
def main():
    passageiro1 = CartaoEmbarque('Ângela Nunes', '235', 'IHHH3M', datetime(2024,11,26,8,56))
    passageiro2 = CartaoEmbarque('Roberto Lemos', '235', 'OMNH5I', datetime(2024,11,26,8,56))
    passageiro3 = CartaoEmbarque('Denise Pereira', '179', 'AOMF9O', datetime(2024,11,22,14,40)) 

    # print(passageiro1)
    # print(passageiro2)
    # print(passageiro3)
    
    print(passageiro1.realizar_check_in())
    # passageiro2.realizar_check_in()
    # passageiro3.realizar_check_in()
    
if __name__=='__main__':
    main()