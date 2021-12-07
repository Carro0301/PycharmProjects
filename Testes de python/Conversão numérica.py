num= int(input('Digite qualquer número: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para BINÁRIO:
[2] Converter para OCTAL:
[3] Converter para HEXADECIMAL:''')
opção = int(input('Essa é sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} comvertido para octal é: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é: {}'.format(num,hex(num)[2:]))
else:
    print('opção inválida: tente novamente!')


