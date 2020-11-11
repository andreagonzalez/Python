#faça um programa que leia um número inteiro qualquer e
#mostre na tela a sua tabuada

n = int(input('Digite um número: '))
i = 0
while(i <= 10):
    mult = n*i
    i = i+1
    print(n, 'x', i-1, '=', mult)