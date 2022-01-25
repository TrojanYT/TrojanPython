alt = float(input('Digite a altura da parede: '))
lag = float(input('Digite a largura da parede: '))
a = alt*lag
l = a/2
print('A área da parede é de {:.2f}m²'.format(a))
print('Você precisará de {:.1f} litros de tinta para pintar {:.2f}m².'.format(l, a))
