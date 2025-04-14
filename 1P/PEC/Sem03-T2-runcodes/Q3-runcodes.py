#Imprimindo conteúdo para o usuário com interação
dividendo = float(input().strip())
divisor = float(input().strip())
#Variantes para fazer cálculos
result1 = dividendo//divisor
result2 = dividendo%divisor
#Imprimindo o resultado na tela do usuário
print(f'{result1:.4f}')
print(f'{result2:.4f}')