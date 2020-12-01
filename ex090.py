'''
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela, se
a média for 7 ou mais ele está aprovado se for menor
está reprovado. No final mostre o conteúdo da estrutura
na tela.'''
alunos = list()
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
alunos.append(dados.copy())
if 5 <= dados['média'] < 7:
    dados['situaçao'] = str('Recuperação')
elif dados['média'] >= 7:
    dados['situaçao'] = str('aprovado')
else:
    dados['situaçao'] = str('reprovado')
for k, v in dados.items():
        print(f'{k} é igual a {v}.')
