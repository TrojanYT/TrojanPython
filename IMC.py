nome = str(input('Digite o seu nome: '))
i = int(input('Digite a sua idade: '))
p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))
imc = p/a**2
print(f"{'':=^20}")
print(f"{'Ficha IMC':^20}")
print(f"{'':=^20}")
print('Nome: {}'.format(nome))
print('Idade: {}'.format(i))
print('Peso: {}kg'.format(p))
print('Altura: {}m'.format(a))
print('IMC: {:.1f}'.format(imc))
if(imc < 18.5):
    print('Status: Você está abaixo do peso!')
elif(imc >= 18.5) and (imc <= 24.9):
        print('Status: Peso Normal!')
elif(imc >= 25) and (imc <= 29.9):
    print('Status: Sobrepeso!')
elif(imc >= 30) and (imc <= 34.9):
    print('Status: OBESIDADE GRAU 1!!!')
elif(imc >= 35) and (imc <= 39.9):
    print('Status: OBESIDADE GRAU 2!!!')
elif(imc >= 40):
    print('Status: OBESIDADE MÓRBIDA!!!'
          ' VOCÊ ESTÁ MORRENDO!!!')
print(f"{'':=^20}")