print('-+-' * 10)
print('Analisando Triângulos ')
print('-+-' * 10)

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os valores acima PODEM FORMAR TRIÂNGULOS')
else:
    print('os valores acima NÃO PODEM FORMAR TRIÂNGULOS')
