'''Crie um programa que leia o nome eo preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar No final mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato'''
continua = ''
preco = mcaro = mbarato = maior = total = cont = 0
prodbarato = ''
prodcaro = ''
while True:
    if continua in 'Ss':
        nome = str(input('Nome do Produto: '))
        preco = float(input('Preço: R$ '))
        continua = str(input('Quer continuar? [S/N]' )).upper().strip()[0]
        cont += 1
        total = total + preco
        if cont == 1:
            mcaro = preco
            mbarato = preco
        if cont > 1:
            if mbarato > preco:
                mbarato = preco
                prodbarato = nome
            if mcaro < preco:
                mcaro = preco
                prodcaro = nome
    else:
        break
print('-'*10)
print('Fim do Programa')
print('-'*10)
print(f'O total da compra foi R$ {total}')
print(f'Temos {prodcaro} custando R$ {mcaro}')
print(f'O produto mais barato foi {prodbarato} que custa R$ {mbarato}')
