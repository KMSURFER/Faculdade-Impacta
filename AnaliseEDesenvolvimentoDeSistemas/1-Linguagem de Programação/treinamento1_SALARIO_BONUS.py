nome = input()
salario_fixo = float(input())
total_vendas = float(input())
total = total_vendas * 0.15
total_geral_com_15 = salario_fixo + total

print(f'TOTAL = R$ {total_geral_com_15:.2f}')
