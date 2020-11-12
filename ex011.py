#faça um programa que leia a largura e altura de uma parede, calcule a área
#e sabendo que cada litro de tinta rende  dois metros quadrados quanta tinta é
#necessária para pintar a parede

l = float(input('Qual a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
latas = area / 2
print('Você precisa de {} litros de tinta'.format(latas))