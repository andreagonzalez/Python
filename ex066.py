'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre el es (desconsiderando o flag)'''
numero = 0
soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um número (use 999 para parar): '))
    if numero == 999:
        break
    soma = numero + soma
    quantidade +=1
print(f'A soma dos {quantidade} números foi {soma} ')
print('FIM DO PROGRAMA!')