sal = float(input('Digite o seu salário correspondente: R$ '))
if sal >= 1250:
    a1 = sal * 0.10
    nsal = sal + a1
    print('O seu salário terá aumento de 10% e o novo salário é de R${:.2f}.'.format(nsal))
elif sal < 1250:
    a2 = sal * 0.15
    nsal = sal + a2
    print('O seu salário terá aumento de 15% e o novo salário é de R${:.2f}.'.format(nsal))