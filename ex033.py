'''faça um programa que leia 3 números e diga qual é o maior e qual é o menor'''

a = int(input('Digite um número inteiro: '))
b = int(input('Digite um segundo número inteiro: '))
c = int(input(('Digite o terceiro número inteiro: ')))

# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = a
if c > a and c > b:
    maior = c
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))