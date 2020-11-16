'''faça um programa que leia o ano e diga se ele é bissexto'''

ano = int(input("Digite o ano que deseja analisar se é bissexto: "))

# Minha solução, não está funcionando para o ano 1900!!!
'''
if ano % 4 == 0:
    if ano % 100 != 0:
        if ano % 400 == 0:
            print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
'''
#Solução do Gustavo Guanabara.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
