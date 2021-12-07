from datetime import date

atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {}  tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Esse é o ano de seu alistamento!')
elif idade > 18:
    saldo = idade - 18
    print("Já passou o tempo do alistamento! Você deveria ter se alistado a {} anos atrás...".format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento!'.format(saldo))
