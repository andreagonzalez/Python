'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o progrma deverá perguntar se o usuário
quer ou não continuar. No final mostrará:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
'''
continua = ''
homens = 0
mulheres = 0
maiores = 0
while True:
    if continua in 'Ss':
        print('-^-' * 7)
        print('CADASTRE UMA PESSOA')
        print('-^-' * 7)
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if idade > 18:
            maiores += 1
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff' and idade < 20:
            mulheres += 1
    else:
        break
print('=' * 10)
print('FIM DO PROGRAMA')
print('=' * 10)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos')

