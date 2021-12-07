r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os valores acima PODEM FORMAR TRIÂNGULOS ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    if r1 != r2 and r2 != r3 and r3 != r1 :
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
     print('Os valores acima NÃO PODEM formar triângulos')
