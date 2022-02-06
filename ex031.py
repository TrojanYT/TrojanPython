km = int(input('Digite a Km que será percorrida na sua viagem? '))
if km <= 200:
    p = km * 0.50
    print('O valor que será pago para percorrer {} km, será de R${:.2f}'.format(km, p))
elif km > 200:
    p = km * 0.45
    print('O valor que será pago para percorrer {}km, será de R${:.2f}'.format(km, p))