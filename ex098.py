'''Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:
a)De 1 até 10, de 1 em 1
b)De 10 até 0, de 2 em 2
c)Uma contagem personalizada.

a saída é no tempo 44:08 do vídeo
'''
from time import sleep

def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(0.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('inicio: '))
fim = int(input('fim:    '))
pas = int(input('passo:  '))
contador(ini, fim, pas)


