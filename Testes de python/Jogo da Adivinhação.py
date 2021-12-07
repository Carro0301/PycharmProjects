from random import randint
from time import sleep
PC =randint(0,5) #PC pensa
print('-=-' * 10)
print('Pensarei em um número entre 0 e 5... Tente adivinhar...')
print('-=-' *10)
jogador =int(input('Em que níumero pensei?...'))
print('PROCESSANDO...')
sleep(2)
if jogador == PC:
    print('Parabéns! Você conseguiu me vencer!')
else:
    var = jogador != PC
    print('Lamento... porém, não foi desta vez!...')
