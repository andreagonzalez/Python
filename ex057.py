'''Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F
Caso esteja errado, peça digitação novamente até ter um valor correto'''
sexo = ''

'''Minha solução
while sexo != 'M' or sexo != 'm'or sexo != 'F' or sexo != 'f':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0] #aqui tira os espaços do início e do fim, passa para
    # maiúscula e pega só a primeira letra(fatiamento)
    if sexo == 'M' or sexo == 'm':
       print('Masculino')
    else:
       if sexo == 'F' or sexo == 'f':
        print('Feminino')
'''
#Solução do Gustavo Guanabara
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, digite o sexo novamente [M/F]: ')).strip().upper()[0]
print('Sexto {} registrado com sucesso'.format(sexo))