#crie um programa que leia quanto dinheiro uma pessoa
#tem na carteira e mostre quantos dólares ela pode comprar

n = float(input('Digite o valor que você tem na carteira? R$ '))
txd = float(input('Qual a taxa do dólar hoje?'))
d = n / txd
print('Você pode comprar {} dólares'.format(d))
