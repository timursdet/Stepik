from math import *
a = float(input())
b = float(input())
avr = float (a+b)/2
geometric_mean = sqrt(a*b)
harmonic_mean = (2*a*b)/(a+b)
root_mean_square = sqrt((pow(a, 2) + pow(b, 2))/2)
print(avr, geometric_mean, harmonic_mean, root_mean_square, sep='\n')
