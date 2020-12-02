'''Crie um programa onde 4 jogadores joguem um dado (1 a6) e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
Colocar pausas entre os resultados'''
from random import randint
from time import sleep
jogo = dict()
jogador = list()
print('Valores sorteados: ')
for i in range(1,5):
    for c in range(1,5):
        num_sort = randint(1, 6)
        jogador.append(jogo.copy())
    print(f'O jogador {i} tirou {num_sort} no dado.')
print('Ranking dos jogadores: ')
# for k, v in jogo.items():
#     print(f'{i}º lugar: jogador {k} com {v}')
#     sleep(1)

# for i in range(1, 5):
#     print(f'{i}º lugar: jogador {jogador} com {num_sort}')


