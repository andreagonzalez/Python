'''Crie um programa que vai ler vários números e colocar numa lista.
Depois disso, crie duas lisas extras que vão contar apenas os valores
pares e os valores ímpares digitados respectivamente.
Ao final mostre o conteúdo das três listas.
'''
continua = ''
digitados = []
par = []
impar = []


while True:
        digitados.append(int(input('Digite um número: ')))
        resp = str(input('Quer continuar? S/N '))
        if resp in 'Nn':
            break
for i, v in enumerate(digitados): #aqui o i é o índice e v é o valor
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Os valores digitados foram: {digitados}')
print(f'Esta é a lista dos números pares: {par}')
print(f'Estes são os números ímpares: {impar}')