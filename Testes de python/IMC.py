Peso = float(input("Digite o peso: "))
Alt = float(input('Digite a altura: '))
IMC = Peso / (Alt** 2)
print('O IMC do cliente está em {:.2f}'. format(IMC))
if IMC <18.5:
    print('O cliente está abaixo do peso ideal')
elif IMC >= 18.5 and IMC < 25:
    print('Você está na faixa de peso ideal')
elif  25<= IMC < 30:
    print('Você está com sobrepeso')
elif 30<= IMC < 40:
    print('Você está OBESO')
elif IMC > 40:
    print('Você está com OBESIDADE MÓRBIDA')
