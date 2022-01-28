import math
a = int(input('Informe o valor do ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('A partir do ângulo {}°, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(a, sen, cos, tg))