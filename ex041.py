'''A Confederação Nacional de Natação precisa um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade
- até 9 anos MIRIM
- até 14 anos INFANTIL
- até 19 anos JÚNIOR
- até 20 anos SENIOR
- acima MASTER'''
from datetime import date
nasc = int(input('Ano nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL.'.format(idade))

elif idade <= 19:
    print('Você tem {} anos e sua categoria é JÚNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos e sua categoria é SÊNIOR.'.format(idade))
elif idade > 20:
    print('Você tem {} anos e sua categoria é MASTER.'.format(idade))