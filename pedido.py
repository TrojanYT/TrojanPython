pedido = str(input('Digite o seu pedido: '))
quant = int(input('Quantidade do pedido: '))
vp = float(input('Valor do Pedido: '))
km = str(input('Acompanha Ketchup e Mostarda? '))
nome = str(input('Nome do cliente: '))
tel = str(input('Telefone: '))
end = str(input('Endereço para entrega: '))
nc = int(input('Número da casa: '))
tx = float(input('Taxa de entrega: '))
pg = str(input('Forma de pagamento: '))
total = vp + tx
print(f"{'':=^21}")
print(f"{'Ex-Burguer Campo Limpo':^21}")
print(f"{'':=^21}")
print(f"{'PEDIDO':^21}")
print(f"{'':=^21}")
print('Pedido: {}x {}'.format(quant, pedido))
print('Acompanha Ketchup e Mostarda: {}'.format(km))
print('Taxa de entrega: R${:.2f}'.format(tx))
print('Total do pedido: R${:.2f} '.format(total))
print(f"{'':=^21}")
print('Nome do cliente: {}'.format(nome))
print('Telefone: {}'.format(tel))
print('Endereço: {}, {}'.format(end, nc))
print('Forma de pagamento: {}'.format(pg))
print(f"{'':=^21}")
