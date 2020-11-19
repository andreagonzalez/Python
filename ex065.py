'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre entre todos os valores
 e qual foi o maior e o menor valor lido. O programa deve perguntar
 ao usuário se ele quer continuar ou ão a digitar valores'''
contador = 0
resposta = 'S'
media = 0
maior = 0
menor = 0
soma = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    contador = contador + 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/contador
print('A média é {}'.format(media))
print('O maior número lido foi {}'.format(maior))
print('O menor valor lido foi {}'.format(menor))
print('Acabou')



