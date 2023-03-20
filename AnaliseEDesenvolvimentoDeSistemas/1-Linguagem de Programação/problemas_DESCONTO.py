# Crie um programa para um site! O programa deverá
# solicitar o valor de um item e a quantidade de
# unidades compradas deste item, ao final deve exibir
# o total com desconto de 10%. Considere que a
# quantidade será um número natural (inteiro) positivo.

valor = float(input('Valor do item: '))
qtd = int(input('Quantidade: '))
total = valor * qtd
desconto = total * 0.10
total_final = total - desconto
print(f'Total com desconto: R$ {total_final:.2f}')
