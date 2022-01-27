d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro percorreu? '))
dp = d*60
kmp = km*0.15
a = dp + kmp
print('O total a pagar fica em: R${:.2f}'.format(a))