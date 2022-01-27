import math
a = int(input('Informe o valor do ângulo: '))
sen = math.sin(a)
cos = math.cos(a)
tg = math.tan(a)
print('A partir do ângulo {}°, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(a, sen, cos, tg))