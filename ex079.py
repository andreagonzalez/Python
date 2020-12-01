'''Crie um progrma onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista não será adicionado. No final,
serão exibidos todos os valore únicos digitados, em ordem crescente'''
continua = ''
valores = []
numero = 0

while True:
    if continua in 'Ss':
        numero = (int(input('Digite um valor: ')))
        if numero not in valores:
            valores.append(numero)
        else:
            print('Número já existe, não vou inseri-lo!')
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    else:
       break
print('Os valores que você digitou são: ', sorted(valores))
