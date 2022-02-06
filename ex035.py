c1 = float(input('Digite o primeiro valor: '))
c2 = float(input('Digite o segundo valor: '))
c3 = float(input('Digite o terceiro valor: '))
if c1 + c2 > c3:
    print('A soma dos lados, formam um triângulo!')
elif (c1 == 0 or c2 == 0 or c3 == 0):
    print('Erro!')
else:
    print('A soma dos lados, não formam um triângulo!')