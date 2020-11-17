'''Crie um programa que leia o ano de nascimento de 7 pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas são maiores de 21 '''
#SOLUÇÃO DO GUSTAVO GUANABARA
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao total tivesmos {} pessoas maiores de idade'.format(totmaior))
print('Ao total tivesmos {} pessoas menores'.format(totmenor))





'''SOLUÇÃO QUE EU ESTAVA FAZENDO, MAS ME ATRAPALHEI
from datetime import date
nascimento = []
atual = date.today().year
idade = atual - nascimento

for c in range(0,6):
    lendo = int(input('Digite a data de nascimento: '))
    nascimento.append(lendo)
print(nascimento)
print(atual)
'''