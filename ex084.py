'''Faça um programa que leia o nome e peso de várias pessoas e guarde tudo
numa lista. No final mostre:
a) Quantas pessoas foram cadastradas
b) Uma lista cos mais pesados
c) Uma lista com os mais leves
'''

lista = []
dados = []
maior = menor = pessoas = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    if len(lista) == 0: #SE AINDA NÃO TEM DADOS CADASTRADOS
        maior = menor = dados[1] #DADOS[0] É O NOME DADOS[1] É O PESO
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:]) #assim criamos uma cópia de dados[:]
    # se fazemos lista.append(dados) ele cria uma ligação das listas
    dados.clear()
    resp = str(input('Quer continuar? S/N '))
    pessoas += 1
    if resp in 'Nn':
        break
print('-+-'*10)
print(f'Você cadastrou {pessoas} pessoas.')
print('-+-'*10)
print(f'O maior peso cadastrado foi {maior}. Peso de ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end=' ')
print()
print('-+-'*10)
print(f'O menor peso informado foi {menor}. Peso de  ', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end=' ')
print()
print(f'Você cadastrou {len(lista)} pessoas') #outra forma de mostrar o
# total de pessoas cadastradas

