'''Faça um progrma que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício indo de 10 a 0, com pausa de 1 segundo entre eles'''
import time

for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
time.sleep(1)
print('0')
time.sleep(1)
print(' Pow! Pum! Pum! Pow')
