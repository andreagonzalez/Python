#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
num_letra = frase.upper()
print('A letra A aparece {} na frase'.format(num_letra.count('A'))) #quantas vezes aparece O maiúsculo
print('A primeira vez que a letra A aparece é na posição {}'.format(num_letra.find('A')+1))
print('A última vez que ela aparece é na posição {}'.format(num_letra.rfind('A')+1))