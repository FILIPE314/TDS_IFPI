#Crie uma classe que defina uma calculadora básica.
#Defina os atributos básicos e implemente os comportamentos(métodos)
#class calculadora:

#    sinal = None
#    num1 = None
#    num2 = None
#    def calculator(self):
#        if self.sinal == 'somar':
#            return self.num1 + self.num2
#        elif self.sinal == 'subtrair':
#            return self.num1 - self.num2
#        elif self.sinal == 'multiplicar':
#            return self.num1 * self.num2
#        elif self.sinal == 'dividir':
#            return self.num1 / self.num2
#def main():
#    resul = calculadora()
#    resul.num1 = float(input('Digite um número para calcular:'))
#    resul.num2 = float(input('Digite outro número para calcular:'))
#    resul.sinal = input('Digite o nome da sua operação:')
#    print(int(resul.calculator()))
#if __name__ == '__main__':
#    main()
 
class calculadora:
    num1 = None
    num2 = None
    sinal = None
    def calculator(self):
        if self.sinal == '+':
            return self.num1 + self.num2
        elif self.sinal == '-':
            return self.num1 - self.num2
        elif self.sinal == '*':
            if self.num1 == 0:
                return 0
            return self.num1 * self.num2
        elif self.sinal == '/':
            if self.num2 != 0:
                return self.num1 / self.num2
def main():
    resul = calculadora()
    while True:
        resul.num1 = float(input('Digite um número para calcular:'))
        resul.num2 = float(input('Digite outro número para calcular:'))
        resul.sinal = input('Digite o símbolo da sua operação:')
        print(int(resul.calculator()))
        print('Quer continuar calculando? (Sim/Não)')
        resposta = input().lower().strip()
        if resposta == 'não' or 'nao':
            print('Encerrando a calculadora!')
            break
if __name__ == '__main__':
    main()