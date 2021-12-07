n1 = float(input('Digite aqui a primeira nota: '))
n2 = float(input('Digite a outra nota: '))
m: float = (n1 + n2) / 2
print(f'A sua média foi: {m:.1f}')
if m >= 6.0:
    print('Nossa! Desta vez você se superou! Parabéns!')
else:
    var = m <= 6.0
    print('Vixe! Você não foi muito bem! Cruz Credo!')
