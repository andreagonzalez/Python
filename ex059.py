'''Crie um programa que leia dois valores e mostre
um menu na tela:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso'''


num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))

print('''Você deseja:
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Números
    [5]Sair do programa''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    soma = num1 + num2
    print('A soma entre {} e {} é {}'.format(num1, num2, soma))
elif opcao == 2:
    multiplica = num1 * num2
    print('A multiplicação entre {} e {} é {}'.format(num1,num2, multiplica))
elif opcao == 3:
    if num1 > num2:
        print('Comparando {} e {} o maior é {}'.format(num1, num2, num1))
    elif num1 < num2:
        print('Comparando {} e {} o maior é {}'.format(num1, num2, num2))
    elif num1 == num2:
        print('Comparando {} e {} eles são iguais'.format(num1, num2))
elif opcao == 5:
    print('Fim')
'''

#Solução do Gustavo Guanabara
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

print('''[1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Números
    [5]Sair do programa''')
opcao = str(input('Qual é sua opção?'))
