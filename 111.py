import math
a = int (input ("Введите сторону 1: "))
b = int (input ("Введите сторону 2: "))
c = int (input ("Введите угол между сторонами: "))
cc = c * math.pi / 180
d = 2
e = 0.5
z = (a ** d) + (b ** d) - (2 * a * b * math.cos(cc))
v = z ** 0.5
print (v)

