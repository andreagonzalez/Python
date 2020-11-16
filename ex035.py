'''Crie um programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triângulo.'''
print('-.-'*9)
print('Conferindo se é Triângulo')
print('-.-'*9)
a = float(input('Digite o valor da reta a: '))
b = float(input('Digite o valor para a reta b: '))
c = float(input('Digite o valor para a reta c: '))

# os testes tem que ser:
# a + b > c
# b + c > a
# a + c > b

if a + b > c and b + c > a and a + c > b:
    print('Essas 3 retas pode sim formar um triângulo')
else:
    print('Essas 3 retas não podem formar um triângulo')