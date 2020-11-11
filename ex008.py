#escreva um programa que leia um valor em metros
#e o exiba convertido em centímetro e milímetros

m = int(input('digite o valor em metros '))
cm = m * 100
mm = m * 1000
print('O valor lido foi {}, o valor em centímetros é {} e em milímetros é {}'.format(m, cm, mm))
