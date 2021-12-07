distancia=float(input('Qual a distância da sua viagem?'))
print('Você está prestes a iniciar uma viagem de {} Km.'.format(distancia))
if distancia <=200:
    preço= distancia * 0.50
else:
    preço= distancia * 0.45
    print('O preço de sua passagem será de {:.2f}'.format(preço))
