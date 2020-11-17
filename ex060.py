'''Faça um programa que leia um número qualquer
e mostre seu fatorial.
Ex: 5!=5x4x3x2x1=120
fazer com while e com for
'''

num = int(input('Digite um número para ver seu fatorial: ')) #5
fat = num
prov = num
while num > 1:
    fat = fat * (num - 1)
    num = num - 1
print('O fatorial de {} vale {}'.format(prov,fat))