'''Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso de zero até
vinte.

Seu progrma deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso'''
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
                'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {extenso[num]}')
    else:
        break
