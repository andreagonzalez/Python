preco = float(input('Qual é o preço de seu produto? R$ '))
total = preco - (preco*0.05)
print('O produto que custava R$ {:.2f},  na promoção com 5% de desconto vai custar R$ {:.2f}'.format(preco, total))