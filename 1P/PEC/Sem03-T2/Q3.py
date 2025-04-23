#Imprimindo conteúdo para o usuário com interação
dividendo = float(input('Esse programa divide qualquer valor que você quiser e mostra o resto que sobra da divisão, coloque o número que você quer dividir:'))
divisor = float(input('E aqui coloque o numero divisor:'))
#Variantes para fazer cálculos
result1 = dividendo//divisor
result2 = dividendo%divisor
#Imprimindo o resultado na tela do usuário
print('Resultado da divisão:', result1)
print('Resultado da sobra da divisão:', result2)