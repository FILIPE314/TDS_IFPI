#Variante para coletar o valor do raio
raio = float(input().strip())
#Variantes para fazer cálculos
cc = 2*3.141592*raio
ac = 3.141592*raio**2
ae = 4*3.141592*raio**2
ve = 4*3.141592*raio**3/3
#Imprimindo o resultado na tela do usuário
print(f'{cc:.6f}')
print(f'{ac:.6f}')
print(f'{ae:.6f}')
print(f'{ve:.6f}')