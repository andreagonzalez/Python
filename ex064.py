'''Crie um programa que leia vários número inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''
cont = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        soma = n + soma -999
    else:
     soma = n + soma
     cont += 1
print('Foram lidos {} números e a soma deles é {}'.format(cont, soma))