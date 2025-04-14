class cadastro_de_veiculos:
    placa = None
    marca = None
    modelo = None
    ano = 0
    cor = None
    proprietario = None
    quiometragem = None

    def __init__(self, p, m, mod, a, c="Não especificada", pro="Não especificada", km="Não especificada"):
        self.placa = p
        self.marca = m
        self.modelo = mod
        self.ano = a
        self.cor = c
        self.proprietario = pro
        self.quilometragem = km

    def __str__(self):
        p = f'Placa do carro: {self.placa}'
        mar = f'Marca do carro: {self.marca}'
        mod = f'Modelo do carro: {self.modelo}'
        ano = f'Ano do carro: {self.ano}'
        c = f'Cor do carro: {self.cor}'
        pro = f'Proprietário do carro {self.proprietario}'
        km = f'Quilômetros rodados {self.quilometragem}'
        return p + mar + mod + ano + c + pro + km
    
def main():
    print('Cadastre seu veículo')
    while True:
        cadas = cadastro_de_veiculos(p = input('Digite a placa:'), m = input('Digite a marca: '), mod = input('Digite o modelo: '), a = input('Digite oano:'),     c = input('Digite a cor: '))
        if cadastro_de_veiculos.cor == 'Não especificada':
            return cadastro_de_veiculos.cor
        else:
            print(cadastro_de_veiculos.cor)
        cadastro_de_veiculos.pro = input('Digite o proprietário: ')
        if cadastro_de_veiculos.proprietario == 'Não especificada':
            return cadastro_de_veiculos.proprietario
        else:
            print(cadastro_de_veiculos.proprietario)
        cadastro_de_veiculos.km = input('Digite a quilometragem: ')
        if cadastro_de_veiculos.quiometragem == 'Não especificada':
            return cadastro_de_veiculos.quiometragem
        else:
            print(cadastro_de_veiculos.quiometragem)
        print(cadas)
if __name__ == '__main__' :
    main()