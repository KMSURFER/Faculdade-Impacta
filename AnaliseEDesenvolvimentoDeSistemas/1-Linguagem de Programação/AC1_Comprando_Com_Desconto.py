"AC1_Comprando_com Desconto"
preco = float(input())

qtd = int(input())

preco_final = preco * qtd

desconto10 = (10 + qtd * 1)/100

x = float(preco_final * desconto10)

desconto1 = float(x * qtd * 0.01)

total_total = float(preco_final - x)


print(f'{preco_final:.2f}')
print(f'{total_total:.2f}')
