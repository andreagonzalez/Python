'''Faça um programa que mostre a soma de todos os números ímpares
que são múltiplos de 3 no intervalo de 1 a 500'''
soma = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        soma = c + soma
        print('Divisível por 3 {}'.format(c))
print('O valor da soma é {}'.format(soma))

