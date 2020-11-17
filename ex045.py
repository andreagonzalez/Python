'''Faça um programa para jogar Jokenpô com o computador'''

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Digite sua escolha:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual sua escolha?'))
print('-+'*10)
if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('GANHEI!!!')
    else:
        print('Jogada inválida. Tente de novo.')
elif computador == 1:
    if jogador ==0:
        print('GANHEI!!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida. Tente de novo.')

elif computador == 2:
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('GANHEI!!!')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida. Tente de novo.')


print('-+'*10)