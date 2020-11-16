'''escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça
ao usuário para tentar descobrir qual foi o número escolhido pelo computador. O computador escreverá
na tela se o usuário venceu ou perdeu'''

import random

numero = int(input('Estou pensando em um número entre 0 e 5. Você consegue adivinhar qual é? Digite seu palpite: ' ))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)

if numero == escolhido:
    print('Você acertou! Parabéns! O número escolhido foi {}'.format(escolhido))
else:
    print('Que pena vocè errou! O número escolhido foi: {}'.format(escolhido))
    print('--- FIM ---')