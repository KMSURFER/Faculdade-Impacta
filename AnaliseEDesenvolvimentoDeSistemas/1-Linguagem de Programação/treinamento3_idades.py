idade = 0
soma = 0
qtd = 0 

while True:
  idade = int(input())
  if idade >= 0:
    soma += idade
    qtd += 1
  else:
       break

print("%.2f" %(soma/float(qtd))) 
