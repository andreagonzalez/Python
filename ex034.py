'''escreva um programa que leia o salário de um funcionário e calcule o valor de seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%'''

atual = float(input('Digite o valor do salário atual: '))

if atual > 1250:
   novo = atual * 1.1
   print('O novo valor é {}'.format(novo))
else:
    novo = atual * 1.15
    print('O novo valor é {}'.format(novo))