'''Refaça o Desafio 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while
'''
#Para achar o enésimo termo da PA --> an = a1+(n-1)*r
#Para somar os n termos da PA --> sn = n(a1+an)/2
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA:'))
n = int(input('Digite o número de termos que deseja ver: '))
todos = []
c = n
an = a1 + ((n -1)*r) #aqui achamos o enésimo termo da PA
seguinte = 0
'''
for c in range(a1, a10+r, r):
    print('{} '.format(c), end= '-> ')
print('ACABOU!')
'''
while c > 0:
    if todos == 0:
        seguinte = a1
    else:
        todos.append(seguinte)
        c = c - 1
        print('O contador C é {}'.format(c))
print('O {} termo da PA é {}'.format(n,an))
print('O primeiro termo da PA é {}'.format(a1))
print(seguinte)