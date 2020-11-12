'''co = float(input('Qual o tamanho do Cateto Oposto? '))
ca = float(input('Qual o tamanho do Cateto Adjacente? '))
h = ((co**2)+(ca**2))**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(h))'''

#resolução utilizando a classe Math -- também pode importar somente o hypot da biblioteca math

import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente '))
h = math.hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(h))

