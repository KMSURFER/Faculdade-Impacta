inicio_ano = int(input())
fim_ano = int(input())
quant_ano_bissexto = 0

if (0 <= inicio_ano <= fim_ano <= 9999):
  while inicio_ano <= fim_ano:
    if (inicio_ano % 4 == 0 and inicio_ano % 100 != 0 or inicio_ano % 400 == 0):
      print(inicio_ano)
      quant_ano_bissexto += 1
    
    inicio_ano += 1
  
  print(f'bissextos: {quant_ano_bissexto}')
