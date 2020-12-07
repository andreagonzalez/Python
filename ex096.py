'''Faça um progrma que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre
a área do terreno'''
def area(l, c):
    total = l * c
    print(f'A área do terreno de {l} x {c} em m² é {total:2}m²')


#Programa Principal
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)

