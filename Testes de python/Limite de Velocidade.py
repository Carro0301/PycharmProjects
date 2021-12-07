Vel = float(input('Qual a velocidade atual do carro?'))
if Vel > 80:
    multa = (Vel - 80) * 7
    print("Você excedeu o limite de velocidade e foi multado em R${:.2f}!".format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
