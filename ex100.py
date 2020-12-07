'''Faça um programa que tenha uma lista chamada números e duas funções
chamddas sorteia() e somaPar(). A primeira função vai sortear 5 números
e ai colocá-los dentro da lista e a segunda função vai mostrar a soma dos
valores Pares sorteados pela função anterior.'''
from random import randint
from time import sleep


def sorteia(lista):
    print('Iniciando o sorteio', end=' ')
    for cont in range(0, 5):
        sorteados = randint(1, 10)
        numeros.append(sorteados)
        print(f'{sorteados}', end=' ', flush=True)
        sleep(0.4)
    print('Sorteio Concluído!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
    print(f'A soma dos números pares é {soma}' )


#Programa Principal

numeros = list()
sorteia(numeros)

somaPar(numeros)
