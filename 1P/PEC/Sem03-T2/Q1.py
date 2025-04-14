#Imprimindo conteúdo para o usuário
print('Pra que perder tempo calculando o comprimento da circunferência, a área de um circulo, a área da esfera e o volume da esfera?')
#Variante para coletar o valor do raio
raio = float(input('Digite aqui o raio:'))
#Variantes para fazer cálculos
cc = 2*3.141592*raio
ac = 3.141592*raio**2
ae = 4*3.141592*raio**2
ve = 4*3.141592*raio**3/3
#Imprimindo o resultado na tela do usuário
print(f'Resultado do comprimento da circunferência:{cc:.6}')
print(f'Resultado da área de um círculo:{ac:.6}')
print(f'Resultado da área da esfera:{ae:.6}')
print(f'Resultado volume da esfera:{ve:.6}')