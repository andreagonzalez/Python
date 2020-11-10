#Faça um programa que leia um número inteiro
#e mostre na tela seu sucessor e seu antecessor

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('O número lido é {}, o antecessor é {} e o sucessor é {}'.format(numero, antecessor, sucessor))
