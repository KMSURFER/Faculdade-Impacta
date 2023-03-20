# Crie um programa que receba como entrada o valor de um produto 
# e a quantidade comprada. O programa concederá 10% de desconto 
# para compras com total maior ou igual à R$ 100,00.
 
valor = float(input('Valor: '))
quantidade = int(input('Quantidade: '))
total = valor * quantidade
 
if total >= 100.0:
    total = total * 0.9
else:
    total = total
 
print('Total:', total)
