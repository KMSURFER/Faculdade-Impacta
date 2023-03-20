v = [5]*7
i = 1
while i < 7:
  if i % 3 == 0:
     v[i] = 2 % i
     i = i + 2
print(v)
