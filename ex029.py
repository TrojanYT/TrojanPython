v = int(input('Informe a velocidade do carro: '))
if v > 80:
    ve = v-80
    m = ve*7
    print('Você ultrapassou o limite de velocidade e por isso foi multado.')
    print('Você deverá pagar a multa no valor de R${:.2f}'.format(m))
else:
    print('Você está dentro do limite de velocidade.')
