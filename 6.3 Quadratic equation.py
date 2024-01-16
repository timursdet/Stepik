from math import *
a, b, c, = float(input()), float(input()), float(input())
d = b**2-4*a*c

if d > 0:
    x1 = (-b + sqrt(d)) /( 2 * a)
    x2 = (-b - sqrt(d)) /( 2 * a)
    if x1 > x2:
        print(x2, x1, sep='\n')
    else:
        print(x1, x2, sep='\n')

elif d == 0:
    x = -b/(2*a)
    print(x)

else:
    print('Нет корней')
