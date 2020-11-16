'''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar: O valor da casa; O salário do comprador; Em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado'''

valor_casa = float(input('Informe o valor do imóvel que você vai comprar R$ '))
salario = float(input('Informe o valor do salário do comprador R$ '))
prazo = int(input('Em quantos anos será feito o pagamento: '))

limite = salario * 0.30
valor_parcela = valor_casa / (prazo*12)

print('valor parcela R$ {:.2f}'.format(valor_parcela))
print('valor máximo permitido R$ {:.2f}'.format(limite))
#print('prazo em anos {}'.format(prazo))

if limite < valor_parcela:
    print('Lamento, mas seu financiamento foi recusado ')
else:
    print('Parabéns! Seu financiamento foi aprovado.')