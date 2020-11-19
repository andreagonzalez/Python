'''Faça um programa que jogue par ou ímar com o computador.
O jogo só será interrompido quando o jogador PERDER mostrando
o total de vitórias consecutivas no final do jogo'''

'''A solução do Gustavo ficou melhor, mas não vou corrigir agora,
pois o meu está funcionando'''
import random
#computador escolhe o número para jogar
#parouimpar = random.choice(['p','i']) #computador escolhe par ou ímpar
#print(parouimpar)

contador = 0
while True:
    escolhido = random.randint(0, 10)
    #print(escolhido)
    print('-*-'* 8)
    print('Vamos jogar PAR ou ÍMPAR')
    print('-*-' * 8)
    jogador = int(input('Digite um valor: '))
    letra = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    soma = escolhido + jogador
    print(f'Você jogou {jogador} e o computador {escolhido}. Total de {soma}')
    if soma %2 == 0 and letra in 'Pp'or soma %2 != 0 and letra in 'Ii':
        print('Você VENCEU!')
        print('Vamos jogar novamente? ')
        contador += 1
    else:
        print('Você PERDEU!')
        print(f'Você ganhou {contador} vezes.')
        break

