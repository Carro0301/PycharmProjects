nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
m = (nota1 + nota2) / 2
if m < 5.0:
    print(' Sua média é {}, e você está REPROVADO'.format(m))
if 7 >m >= 5.0 :
    print('Sua  média é {}, e você está em RECUPERAÇÃO'.format(m))
if m > 7.0:
    print('Sua média é {} e você está APROVADO'.format(m))
