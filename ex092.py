'''Crie um programa que leia nome, ano de nascimento e a carteira de trabalho e
cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de
zero o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import date
atual = date.today().year

cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['ano-nasc'] = int(input('Ano Nascimento: '))
cadastro['carteira'] = int(input('Carteira de trabalho (0 = não tem): '))
cadastro['idade'] = atual - cadastro['ano-nasc']
if cadastro['carteira'] == 0:
    for k, v in cadastro.items():
        print(f'- {k} tem valor {v}')
else:
    cadastro['contrato'] = int(input('Ano Contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposenta'] = cadastro['idade'] + ((cadastro['contrato'] + 35) - atual)
    for k, v in cadastro.items():
        print(f' - {k} tem valor {v}')

