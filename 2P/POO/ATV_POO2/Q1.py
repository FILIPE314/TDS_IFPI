class relogio_digital_simples:
    hora = 0
    minuto = 0
    def __init__(self, hr, min):
        self.hora = hr
        self.minuto = min
    def result(self):
        if self.hora < 24 and self.minuto < 60:
            return f'{self.hora}' + ':' + f'{self.minuto}'
        else:
            return 'valor inválido'
        
def main():
    print('Oi, quer digitar as horas e minutos de um relógio? Se quiser sair digite (60) no minuto.')
    while True:
        hr = int(input('Digite a hora aqui:'))
        min = int(input('Digite os minutos aqui:'))
        relogio = relogio_digital_simples(hr, min)
        if relogio.minuto == 60:
            break
        else:
            print(relogio.result())
if __name__ == '__main__':
    main()