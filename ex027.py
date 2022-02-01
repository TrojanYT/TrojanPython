nome = str(input('Digite o seu nome completo: ')).upper().strip()
n = nome.split()
print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n.pop()))
