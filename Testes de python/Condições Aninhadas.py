Valor= float(input('Qual o valor da casa? '))
Salário= float(input('Qual o salário? '))
anos = int(input("Quantos anos de fianciamento? "))
prestação = Valor / (anos * 12)
mínimo = Salário * 30 / 100
print('Para pagar o valor de R$ {:.3f} da casa em {} anos, '.format(Valor, anos))
print('a prestação será de R$ {:.3f} '.format(prestação))
if  prestação <= mínimo:
    print('Prestação PODE ser concedida')
else:
    print( 'Empréstimo NEGADO!')