#Cria um programa que leia o nome de uma pessoa e diga se ela tem SILVA
#no nome, ou seja, início fim ou meio

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) #o in é um operador do Python
