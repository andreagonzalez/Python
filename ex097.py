'''Faça um programa que tenha uma função chamada excreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex.:
escreva('Olá Mundo')
Saida:
----------
Olá Mundo!
----------

Obs.: O tracejado tem que acompanhar o tamanho do texto que será escrito

'''
cont = x = 0
def escreva(texto, cont):
    print('-' * cont)
    print(texto)
    print('-' * cont)


texto = str(input('Digite algo: ')).strip()
for x in range(cont, len(texto)):
    cont = cont + 1
escreva(texto, cont)






# nome = str(input('Digite seu nome completo: ')).strip() #a função strip elimina os espaços antes e depois da frase, mas não no meio das palavras
# dividido = nome.split()
#
# print('Analisando o seu nome...')
#
# print('Seu nome em maíusculas é: {}'.format(nome.upper())) #todas as letras maiúsculas
# print('Seu nome em minúsculas é: {}'.format(nome.lower())) #todas minúsculas
# print('Seu nome tem {} letras'.format(len(nome) - nome.count(' '))) #quantas letras tem no total (menos os espaços)
# print('Seu primeiro nome tem {} letras'.format(len(dividido[0]))) #mostra o tamanho de dividido
# print('O seu primeiro nome é {}'.format(dividido[0])) #quantas letras tem o primeiro nome