def dataDivida(salario, divida):
    ano = 2016
    mes = 10
    mesDivida = 1
    contador = 0
    dividaFinal = divida
    while True:
        if dividaFinal > salario: break

        if mes == 3: salario = salario + (salario * (5/100))

        dividaFinal = divida * (15/100 + 1) ** mesDivida

        mes = mes + 1
        if mes > 12: 
            mes = 1
            ano = ano + 1
        mesDivida = mesDivida + 1
        contador = contador + 1
    return  mes, ano

def main():
    salario = float(input().strip())
    divida = float(input().strip())

    dataFinal = dataDivida(salario, divida)
    print(f'{dataFinal[0]}/{dataFinal[1]}')

if __name__ == '__main__':
    main()