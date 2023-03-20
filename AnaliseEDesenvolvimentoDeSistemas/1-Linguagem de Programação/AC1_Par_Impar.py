num = int(input())
if num % 2 == 0:
    par = num + 2
    impar = num - 1
else:
    par = num + 1
    impar = num - 2
print(f'{impar}', end=' ')
print(f'{par}')
