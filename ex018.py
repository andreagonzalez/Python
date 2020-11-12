import math

ang = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O valor do seno é {:.2f}, do cosseno {:.2f} e da tangente {:.2f}.'.format(seno, cos, tg))