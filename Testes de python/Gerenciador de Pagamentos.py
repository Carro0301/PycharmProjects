print('{:=^40}'.format(' STREPPEL S/A '))
preço = float(input('Preço das compras: R$ '))
print('''Formas de pagamento
[1] à Vista, dinheiro ou cheque
[2] cartão a vista
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual a opção?'))
if opção == 1:
   total= preço - ( preço * 10 / 100)
elif opção == 2:
    total= preço - (preço * 5 /100)
    print('Sua compra de R${:.2f} custará R${:.2f} com o desconto final.'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print( 'Sua compra de {}, será parcelada em 2x de R${} no cartão.'.format(preço, parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'. format(totparc, parcela))
else
    total= 0
    print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE')
print('Sua compra de R${:.2f} custará  R${:.2f} ao final.'.format(preço, total))

