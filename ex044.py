'''Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento

- à vista dinheiro / cheque: 10% de desconto
- à vista no catão: 5% de desconto
- em até 2x no catão: preço normal
- 3x ou mais no catão: 20% de juros'''
print('{:=^40}'.format('LABFIS EQUIPAMENTOS CIENTÍFICOS'))
preco = float(input('Digite o valor do produto: R$ '))
forma_pgto = int(input('''Selecione a forma de pagamento:
[1] à vista
[2] até 2x no cartão
[3] 3x ou mais no cartão 
'''))
if forma_pgto == 1:
    valor = preco - (preco*0.10)
    print('O valor do produto é R$ {:.2f}, para pagamento à vista tem 10% de desconto, então você vai pagar R$ {:.2f}'.format(preco, valor))
elif forma_pgto == 2:
    valor = preco - (preco*0.05)
    print('O valor do produto é R$ {:.2f}, para pagamento à vista no cartão seu desconto é de 5%, o novo valor é R$ {:.2f}'.format(preco, valor))
elif forma_pgto == 3:
    valor = preco + (preco*0.20)
    print('O valor original do produto é R$ {:.2f}, para pagamento no cartão em 3x ou mais o novo valor é R$ {:.2f}.'.format(preco, valor))
else:
    print('Opção inválida. Tente novamente.')