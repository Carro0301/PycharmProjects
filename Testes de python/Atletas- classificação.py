from datetime import date
atual = date.today().year
nasc = int (input('Ano de Nascimento: '))
idade = atual-nasc
print('O atleta tem {} anos de idade'.format(idade))
if idade <= 9:
    print('Classidficação MIRIM')
elif idade <=14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação JUNIOR')
elif idade <=25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')