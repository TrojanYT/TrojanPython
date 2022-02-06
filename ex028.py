import random
import time
print(f"{'':=^21}")
print(f"{'JOGO DA ADVINHAÇÃO':^21}")
print(f"{'':=^21}")
n = int(input('Qual o número que eu estou pensando, entre 0 e 5? '))
print('PROCESSANDO...')
time.sleep(3)
lista = [0, 1, 2, 3, 4, 5]
nc = random.choice(lista)
print('O número que eu pensei foi, o número {}.'.format(nc))
if n == nc:
    print('Certa Resposta!')
else:
    print('Que pena, você errou!')