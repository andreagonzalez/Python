'''Melhore o jogo do desafio 28 onde o computador vai pensar
em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer'''
'''Minha solução
import random
numero = 0
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(lista)
contador = 1
while numero != escolhido:
    numero = int(input('Estou pensando em um número entre 0 e 10. Você consegue adivinhar qual é? Digite seu palpite: '))
    if numero != escolhido:
        print('Que pena vocè errou! Tente novamente!')
        contador = contador +1
else:
        print('Você acertou! Parabéns! O número escolhido foi {}'.format(escolhido))
        print('Foram {} tentativas até você acertar'.format(contador))
        print('---> FIM <--')
'''
#Solução do Gustavo Guanabara
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. Parbéns!'.format(palpites))
