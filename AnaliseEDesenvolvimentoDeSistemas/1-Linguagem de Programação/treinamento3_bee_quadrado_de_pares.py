n = int(input())
x = 2
while x <= n:
    if(x % 2 == 0):
      x_2 = x**2
      print(f'{x}^2 = {x_2}')
    x += 1
