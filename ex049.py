'''Refaça o exercício desafio 09, mostrando a tabuada do número
que o usuário escrever, só que agora usando o for'''

num = int(input('Digite um número para saber sua tabuada: '))
for c in range(1,11):
    print('{} x {} = {}'.format(c, num, num*c))
