#Faça um programa que leia o nome completo de uma pessoa, mostrando em
#seguida o primeiro e o último nome separadamente.
#Ex. primeiro=Ana segundo=Maria
#Ex. Andrea Veronica González... primeiro=Andrea último=González

nome_comp = str(input('Digite seu nome completo: ')).strip().upper()
nome = nome_comp.split()

print('Seu nome completo é {}'.format(nome_comp))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

