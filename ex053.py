'''Crie um programa que leia uma frase qualquer e diga se ela
é um palindromo, desconsiderando os espaços'''

frase =str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] #FATIAMENTO

'''Para fazer o mesmo exercício sem FOR:
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto,inverso)
'''
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é palíndromo')


'''
nova1 = frase.replace(' ', '')
tam = len(nova1)
reverso = reversed(nova1)
print(nova1)
print(tam)
print(reverso)
#for c in range(0,tam):
'''


