'''Crie um programa que leia um nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
notas = list()
dados = list()
nota1 = nota2 = media = 0
cont = 0
while True:
        dados.append(str(input('Digite o nome do aluno: ')))
        nota1 = (float(input('Primeira nota: ')))
        nota2 = (float(input('Segunda nota: ')))
        media = (nota1 + nota2)/2
        dados.append(nota1)
        dados.append(nota2)
        dados.append(media)
        notas.append(dados[:])
        dados.clear()
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if continua in 'Nn':
            break
print('*' * 40)
print(f'{"No.":<4}{"Nome":<10}{"Média":>0}')
print('*' * 40)
for i, n in enumerate(notas):
    #print(f'{i+1} {notas[i]}')
    print(f'{i:<4}{n[0]:<10}{n[2]:>8.1f}')
while True:
    print('-' * 40)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(notas):
        print(f'Notas de {notas[opcao]}')


