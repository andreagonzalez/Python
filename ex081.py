'''Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, mostre:

a)Quantos números foram digitados
b)A lista de valores em ordem decrescente
c) Se o valor 5 foi digitado e está ou não
na lista'''
continua = ''
valores = []
numero = 0
cont = 0
while True:
    if continua in 'Ss':
            numero = (int(input('Digite um valor: ')))
            valores.append(numero)
            continua = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            cont += 1
    else:
        break
if 5 in valores:
     print('O número 5 faz parte da lista')
valores.sort(reverse=True)
print(f'Você digitou {cont} números!')
print( f'Os valores em ordem decrescente são: {valores}')
print('Os valores que você digitou são: ', sorted(valores))
