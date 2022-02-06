import calendar
ano = int(input('Digite um ano qualquer: '))
anob = calendar.isleap(ano)
if anob == True:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')