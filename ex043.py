'''Faça um programa que leia a altura e o peso da pessoa e calcule o IMC,
e mostre seu status de acordo com a tabela abaixo:
- Abaixo de 18,5: abaixo do peso
- Entre 18,5 e 25: peso ideal
- De 25 a 30: sobrepeso
- De 30 até 40: obsisdade
- Acima de 40: obesidade mórbida
obs. IMC = peso(kg) / (altura)** m
'''

altura = float(input('Digite sua altura (m):  '))
peso = float(input('Digite o seu peso (kg): '))
imc = peso / (altura*altura)

if imc < 18.5:
    print('O seu peso é {} kg, então você está abaixo do peso. Seu IMC é {:.1f}.'.format(peso, imc))
elif 18.5 <= imc < 25:
    print('Seu peso é {} kg, você está com o peso ideal. Parbéns, seu IMC é {:.1f}!'.format(peso, imc))
elif 25 <= imc < 30:
    print('Seu peso é {} kg, você está com sobrepeso, seu IMC é {:.1f}.'.format(peso, imc))
elif 30 <= imc <= 40:
    print('Seu peso é {} kg, você está com obesidade, pois seu IMC é {:.1f}.'.format(peso, imc))
elif imc > 40:
    print('Seu peso é {} kg, então você está com obesidade mórbida. Tome cuidado, seu IMC é {:.1f}.'.format(peso, imc))
