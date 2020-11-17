'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
de acordo com média atingida
 - Média abaixo de 5, REPROVADO
 - Média entre 5.0 e 6.9, RECUPERAÇÃO
 - Média 7.0 ou superior, APROVADO'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Sua média é {} e você foi Reprovado.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Você ficou com média {} e deverá fazer Recuperação.'.format(media))
elif media >= 7:
    print('Sua média é {} e você está Aprovado,'.format(media))
