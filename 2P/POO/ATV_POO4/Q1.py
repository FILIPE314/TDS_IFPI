class cnh:

    def __init__(self, nome, identidade, cpf, dtn, cat_hab, n_registro, validade, dt_emi, hab_1 = 'Não definido', obs = 'Não definido', local = 'Não definido'):
        self.nome = nome
        self.identidade = identidade
        self.cpf = cpf
        self.dtn = dtn
        self.cat_hab = cat_hab
        self.n_registro = n_registro
        self.validade = validade
        self.dt_emi = dt_emi
        self.hab_1 = hab_1
        self.obs = obs
        self.local = local
        
    def mudar1(self, hab_1):
        if self.hab_1 != None:
            return hab_1
    def mudar2(self, obs):
        if self.obs != None:
            return obs
    def mudar3(self, local):
        if self.local != None:
            return local
    def validar_categoria(self, cat_hab):
        if cat_hab.upper() in 'ABACADAE':
            self.categoria = cat_hab.upper()
        else: raise ValueError('Digite uma categoria existente!')

    def __str__(self):
        r1 = f'Nome: {self.nome}\n'
        r2 = f'Identidade: {self.identidade}\n'
        r3 = f'CPF: {self.cpf}\n'
        r4 = f'Data de nascimento: {self.dtn}\n'
        r5 = f'Tipo de carteia: {self.cat_hab}\n'
        r6 = f'Número de registro: {self.n_registro}\n'
        r7 = f'Data de validade: {self.validade}\n'
        r8 = f'Data de emissão: {self.dt_emi}\n'
        r9 = f'Primeira habilitação: {self.hab_1}\n'
        r10 = f'Observação: {self.obs}\n'
        r11 = f'Local: {self.local}'
        return r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11
def main():
    minha_cnh = cnh('Luiz Filipe', '546.253.486-12', '546.253.486-12', '04/08/2025', 'AB', '546.253', '04/08/2035', '04/08/2024')
    print(minha_cnh)
    while True:
        opcao = int(input('''\nEscolha uma opção:
     1  Alterar nome
     2  Mudar categoria
     3  Acrescentar observações
     4  Editar o local
     5  Encerrar
        --'''))
        if opcao == 1:
            minha_cnh.nome = input('\nDigite o nome: ')
        elif opcao == 2:
            tipo = input('\nDigite a nova categoria: ')
            minha_cnh.validar_categoria(tipo)
        elif opcao == 3:
            minha_cnh.observacoes = input('\nDigite as observações: ')
        elif opcao == 4:
            minha_cnh.local = input('\nDigite um novo local: ')
        elif opcao == 5: 
            break
        print(minha_cnh)
if __name__ == '__main__':
    main()