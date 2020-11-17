'''Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa PA'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA:'))
#Para achar o enésimo termo da PA --> an = a1+(n-1)*r
#Para somar os n termos da PA --> sn = n(a1+an)/2
a10 = a1 + (10-1) * r
for c in range(a1, a10+r, r):
    print('{} '.format(c), end= '-> ')
print('ACABOU!')
