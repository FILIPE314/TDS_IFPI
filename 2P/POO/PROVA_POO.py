#LUIZ FILIPE DE CARVALHO
#THIARIO DE LIMA SILVA

class MaquinaDeCafe:
    def __init__(self, capacidade_reservatorio, tipo_cafe='expresso', temperatura=80, nivel_agua=0):
        self.capacidade_reservatorio = capacidade_reservatorio  
        self._nivel_agua = nivel_agua  
        self._tipo_cafe = tipo_cafe  
        self._temperatura = temperatura  
        self._ligado = False

    # Getters e Setters para os atributos encapsulados
    @property
    def nivel_agua(self):
        return self._nivel_agua

    @nivel_agua.setter
    def nivel_agua(self, valor):
        if valor < 0:
            print("Nível de água não pode ser negativo.")
        elif valor > self.capacidade_reservatorio:
            self._nivel_agua = self.capacidade_reservatorio
            print(f"Nível de água ajustado para a capacidade máxima: {self.capacidade_reservatorio}ml.")
        else:
            self._nivel_agua = valor

    @property
    def tipo_cafe(self):
        return self._tipo_cafe

    @tipo_cafe.setter
    def tipo_cafe(self, tipo):
        tipos_validos = ['expresso', 'cappuccino', 'latte']
        if tipo in tipos_validos:
            self._tipo_cafe = tipo
        else:
            print("Tipo de café inválido. Escolha entre: expresso, cappuccino, latte.")

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 70 <= valor <= 100:
            self._temperatura = valor
        else:
            print("Temperatura inválida. A temperatura deve estar entre 70 e 100°C.")

    @property
    def ligado(self):
        return self._ligado

    @ligado.setter
    def ligado(self, valor):
        if isinstance(valor, bool):
            self._ligado = valor
        else:
            print("Valor inválido para 'ligado'. Deve ser True ou False.")
    
    # Métodos da classe
    def ligar(self):
        self.ligado = True
        print(f'Máquina ligada. Estado atual: {self.estado_atual()}')
    
    def desligar(self):
        self.ligado = False
        print(f'Máquina desligada. Estado atual: {self.estado_atual()}')
    
    def adicionar_agua(self, quantidade):
        if quantidade <= 0:
            print('Quantidade inválida de água.')
            return
        
        novo_nivel = self.nivel_agua + quantidade
        if novo_nivel > self.capacidade_reservatorio:
            self.nivel_agua = self.capacidade_reservatorio
            print(f'O reservatório está cheio. A água foi ajustada para {self.capacidade_reservatorio}ml.')
        else:
            self.nivel_agua = novo_nivel
            print(f'Água adicionada. Nível atual de água: {self.nivel_agua}ml.')
    
    def aquecer_agua(self, temperatura):
        self.temperatura = temperatura  
        print(f'Temperatura ajustada para {self.temperatura}°C.')
    
    def selecionar_tipo(self, tipo):
        self.tipo_cafe = tipo  
        print(f'Tipo de café selecionado: {self.tipo_cafe}.')
    
    def preparar_cafe(self):
        if not self.ligado:
            print('A máquina está desligada. Ligue-a para preparar o café.')
            return
        
        if self.nivel_agua <= 0:
            print('Não há água suficiente para preparar o café.')
            return
        
        if not (70 <= self.temperatura <= 100):
            print('A temperatura da água não está adequada para preparar o café.')
            return
        
        print(f'Preparando {self.tipo_cafe}... Café pronto! Nível de água restante: {self.nivel_agua}ml.')
        self.nivel_agua -= 50
    
    def estado_atual(self):
        return f'Nível de água: {self.nivel_agua}ml, Temperatura: {self.temperatura}°C, Tipo de café: {self.tipo_cafe}, Ligada: {self.ligado}'

def main():
    # Criação de três objetos da classe MaquinaDeCafe
    maquina1 = MaquinaDeCafe(capacidade_reservatorio=1000, tipo_cafe='expresso', temperatura=80, nivel_agua=200)
    maquina2 = MaquinaDeCafe(capacidade_reservatorio=1200, tipo_cafe='cappuccino', temperatura=75, nivel_agua=500)
    maquina3 = MaquinaDeCafe(capacidade_reservatorio=800, tipo_cafe='latte', temperatura=90, nivel_agua=300)

    # Exibindo os estados iniciais
    print('Estado inicial da máquina 1:')
    print(maquina1.estado_atual(), "\n")
    print('Estado inicial da máquina 2:')
    print(maquina2.estado_atual(), "\n")
    print('Estado inicial da máquina 3:')
    print(maquina3.estado_atual(), "\n")

    # Simulando o uso da máquina
    maquina1.ligar()
    maquina1.adicionar_agua(300)  
    maquina1.aquecer_agua(95)  
    maquina1.selecionar_tipo('latte')  
    maquina1.preparar_cafe()  

    # Exibindo os estados finais
    print('Estado final da máquina 1:')
    print(maquina1.estado_atual(), "\n")

    maquina2.ligar()
    maquina2.adicionar_agua(200)
    maquina2.aquecer_agua(85)
    maquina2.selecionar_tipo('expresso')
    maquina2.preparar_cafe()

    print('Estado final da máquina 2:')
    print(maquina2.estado_atual(), "\n")

    maquina3.ligar()
    maquina3.adicionar_agua(100)
    maquina3.aquecer_agua(72)
    maquina3.selecionar_tipo('cappuccino')
    maquina3.preparar_cafe()

    print('Estado final da máquina 3:')
    print(maquina3.estado_atual())
if __name__ == '__main__':
    main()