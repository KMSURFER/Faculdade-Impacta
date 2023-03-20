a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

triang_area = (a * c)/2
circ_area = pi * c**2
trap_area = ((a+b)*c)/2
quad_area = b**2
retang_area = a*b

print(f'TRIANGULO: {triang_area:.3F}')
print(f'CIRCULO: {circ_area:.3F}')
print(f'TRAPEZIO: {trap_area:.3F}')
print(f'QUADRADO: {quad_area:.3F}')
print(f'RETANGULO: {retang_area:.3F}')

