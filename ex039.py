'''Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
- Se ele ainda vai se alistar ao serviço militar
- Se é hora de se alistar
- Se ele já passou do tempo de alistamento
O programa deverá ainda mostrar o tempo que falta ou o que passou do prazo'''

from datetime import date

atual = date.today().year
nasc = int(input('Em qual ano você nasceu? '))
idade = atual - nasc
prazo = idade - 18

if idade == 18:
    print('Você tem {} anos e deve fazer o alistamento até junho de {}'.format(idade, atual))
elif idade > 18:
    print('Você tem {} anos e já deve ter feito o seu alistamento há {} anos'.format(idade, prazo ))
else:
    print('Você tem {} anos e ainda faltam {} para seu alistamento'.format(idade, prazo))

