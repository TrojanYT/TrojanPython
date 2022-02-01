nome = str(input('Digite o seu nome completo: ')).strip()
n = (nome.upper().find('SILVA'))
if(n <= -1):
    print('Não há Silva no nome informado.')
elif(n >= 0):
    print('No nome informado acima, há Silva!')