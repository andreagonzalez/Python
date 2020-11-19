'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número for negativo'''
num = 0
while True:
    print('-'*30)
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{c} x {num} = {num*c}')
print('-*-*- Fim de Programa -*-*-')

