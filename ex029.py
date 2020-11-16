'''escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar a velocidade de 80km/h escreva que ele foi multado
A multa vai custar R$ 7 para cada km acima do limite'''


velocidade = int(input('Digite a velocidade do carro: '))
multa = velocidade - 80
valor_multa = multa * 7
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade de 80 km/h e o valor de sua multa é R$ {}'.format(valor_multa))
else:
    print('Você está dentro do limite de velocidade.')
