n = float(input('Quantos reais (R$), você tem na carteira? '))
dol = n / 3.27
print('Com R${:.2f}, você pode comprar ${:.2f}'.format(n, dol))