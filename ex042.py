'''Refaça o exercício 35 dos triângulos acrescentando o recurso  de mostrar
que tipo de triãngulo será formado
- Equilátero: todos os lados iguais
- Isóceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
print('-.-' * 9)
print('Classificando um Triângulo ')
print('-.-' * 9)
a = float(input('Digite o valor da reta a: '))
b = float(input('Digite o valor para a reta b: '))
c = float(input('Digite o valor para a reta c: '))

# os testes tem que ser:
# a + b > c
# b + c > a
# a + c > b

if a + b > c and b + c > a and a + c > b and a == b and a == c:
    print('Equilátero')
elif a + b > c and b + c > a and a + c > b and a != b and a != c and b != c:
    print('Escaleno')
elif a + b > c and b + c > a and a + c > b and a == b and a != c or a == c and a != b or b == c and b !=a:
    print('Isóceles')
else:
    print('Essas 3 retas não podem formar um triângulo')