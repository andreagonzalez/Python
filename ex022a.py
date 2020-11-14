#Crie um programa que leia o nome compelto de uma pessoa e mostre:
#todas as letras maiúsculas
#todas minúsculas
#quantas letras ao total sem considerar espaços
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip() #a função strip elimina os espaços antes e depois da frase, mas não no meio das palavras
dividido = nome.split()

print('Analisando o seu nome...')

print('Seu nome em maíusculas é: {}'.format(nome.upper())) #todas as letras maiúsculas
print('Seu nome em minúsculas é: {}'.format(nome.lower())) #todas minúsculas
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' '))) #quantas letras tem no total (menos os espaços)
print('Seu primeiro nome tem {} letras'.format(len(dividido[0]))) #mostra o tamanho de dividido
print('O seu primeiro nome é {}'.format(dividido[0])) #quantas letras tem o primeiro nome


