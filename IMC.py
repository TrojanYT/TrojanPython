nome = str(input('Digite o seu nome: '))
p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))
imc = p/a**2
if(imc < 18.5):
    print('Você está abaixo do peso!')
elif(imc >= 18.5) and (imc <= 24.9):
        print('Peso Normal!')
elif(imc >= 25) and (imc <= 29.9):
    print('Sobrepeso!')
elif(imc >= 30) and (imc <= 34.9):
    print('OBESIDADE GRAU 1!!!')
elif(imc >= 35) and (imc <= 39.9):
    print('OBESIDADE GRAU 2!!!')
elif(imc >= 40):
    print('OBESIDADE MÓRBIDA!!! VOCÊ ESTÁ MORRENDO!!!')
print('{}, o seu IMC é de: {:.1f}'.format(nome, imc))