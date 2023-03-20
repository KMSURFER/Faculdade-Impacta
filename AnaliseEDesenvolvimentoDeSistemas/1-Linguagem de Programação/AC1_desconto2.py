preco = float(input())
qtd = int(input())

preco_final = float (preco * qtd)

descont10 = float (preco_final * 0.10)

descont1 = float(desconto10 * qtd * 0.01)

total = float(x - descont1) 


print(f'{total:.2f}')
print(f'{total_final:.2f}')

