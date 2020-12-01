'''Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar
quantas cédulas de cada valor serção entregues
OBS. Considere que o caixa possui cédulas de R$ 50, R$20, R$10
e R$1'''
ced1 = ced2 = ced5 = ced10 = ced20 = ced50 = ced100 = 0
print('='*25)
print('{:^30}'.format('BANCO AVG')) #o trecho entre chaves centraliza
print('='*25)
valor = int(input('Qual valor quer sacar? R$ '))
while valor > 0:
    if valor >= 100:
        ced100 = ced100 + 1
        valor = valor - 100
    elif valor >= 50:
        ced50 = ced50 + 1
        valor = valor - 50
    elif valor >= 20:
        ced20 = ced20 + 1
        valor = valor - 20
    elif valor >= 10:
        ced10 = ced10 - 1
        valor = valor - 10
    elif valor >= 5:
        ced5 = ced5 + 1
        valor = valor - 5
    elif valor >= 2:
        ced2 = ced2 + 1
        valor = valor - 2
    elif valor >= 1:
        ced1 = ced1 + 1
        valor = valor - 1
print(f'A quantidade de notas de 100 é {ced100}, de cédulas de 50 é {ced50}, '
      f'de 20 é {ced20}, de 10 é {ced10}, de 5 é {ced5}, de 2 é {ced2} e de 1 é {ced1}')
