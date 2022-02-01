frase = str(input('Digite um frase: ')).strip().upper()
print('Na frase {}, há {} letras a.'.format(frase, frase.count('a')))
print('Na frase {}, a letra a, aparece a primeira vez na posição {}.'.format(frase, frase.find('a')))
print('Na frase {}, a letra a, aparece a última vez na posição {}.'.format(frase, frase.rfind('a')))