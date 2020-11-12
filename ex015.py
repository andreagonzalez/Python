km = float(input('Quantos km o carro percorreu?'))
dias = int(input('Por quantos dias o carro foi alugado'))
pagar = (km * 0.15) + (dias * 60)
print('O valor a pagar é {:.2f}'.format(pagar))