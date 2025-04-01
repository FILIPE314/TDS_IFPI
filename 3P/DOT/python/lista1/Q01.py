# =============================================================================================================================================================
# Questão 1
def par_ou_impar(num):
    if num % 2 == 0:
        return True
    else: 
        return False
def main():
    while True:
        try:
            num = int(input('Digite um número:'))
            if par_ou_impar(num):
                print("\nO número %d é par." % num)
            else:
                print("\nO número %d é ímpar." % num)
            break
        except:
            print('\nDigite um valor válido!')
if __name__ == '__main__':
    main()