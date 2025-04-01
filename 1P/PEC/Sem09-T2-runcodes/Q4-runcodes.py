# função que calcula quanto o cliente gastou com morango
def gasto(morango_kg):
    if morango_kg > 5.0:
        return 2.20 * morango_kg
    else:
        return 2.50 * morango_kg
# função que calcula quanto o cliente gastou com maçã
def gasto2(maca_kg):
    if maca_kg > 5.0:
        return 1.50 * maca_kg
    else:
        return 1.80 * maca_kg
# função que calcula o total gasto com desconto se for o caso
def total(kg_total,total_gasto):
    if kg_total > 8 or total_gasto > 25.00:
        return total_gasto - (total_gasto * 0.10)
    else:
        return total_gasto
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    morango_kg = float(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    maca_kg = float(input().strip())
    # variável que armazena dados
    mo = gasto(morango_kg)
    # variável que armazena dados
    ma = gasto2(maca_kg)
    # variável que calcula e armazena dados
    total_gasto = mo + ma
    # variável que calcula e armazena dados
    kg_total = morango_kg + maca_kg
    # imprime o resultado da função
    print(f'{total(kg_total,total_gasto):.2f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()