'''escreva um programa que leia um número e mostre na tela se é par ou ímpar'''

numero = int(input('Digite um número: '))

resto = numero % 2

if resto == 0:
    print('O número que você digitou é PAR')
else:
    print('o número é ÍMPAR')
