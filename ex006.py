#Crie um algoritmo que leia um número e mostre
#seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = d + n
e = n ** (1/2)
print('O número lido foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(n, d, t, e))