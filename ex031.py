'''escreva um programa que pergunte a distância de uma viagem em km.
Calcule o preço de uma passagem, cobrando R$ 0,50 por km para viagens até 200km e
e 0,45 para vaigens mais longas'''

distancia = int(input('Digite a distância da viagem que deseja calcular: '))
valor1 = distancia * 0.50
valor2 = distancia * 0.45

if distancia >= 200:
    print('Sua viagem vai custar {}'.format(valor2))
else:
    print("Sua viagem vai custar R$ {}".format(valor1))
