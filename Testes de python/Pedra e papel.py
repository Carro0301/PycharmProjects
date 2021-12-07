from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint (0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
Jogador = int(input('Qual é a sua jogada?'))
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' *15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[Jogador]))
print('-=' * 15)
if computador == 0: # computador jogou PEDRA
    if Jogador ==0:
        print('EMPATE')
    elif Jogador ==1:
        print('Jogador VENCE')
    elif Jogador ==2:
        print('Computador VENCE')
    else:
        print('Jogada Inválida')
elif computador ==1: # computador jogou PAPEL
    if Jogador ==0:
        print('Computador VENCE')
    elif Jogador ==1:
        print('EMPATE')
    elif Jogador ==2:
        print('Jogador VENCE')
    else:
        print('Jogada Inválida')
elif computador ==2: # computador jogou TESOURA
    if Jogador ==0:
        print('Jogador VENCE')
    elif Jogador ==1:
        print('Computador VENCE')
    elif Jogador ==2:
        print('EMPATE')
    else:
        print('Jogada Inválida')

