from math import *
total = 0
n = int(input())
for i in range(1, n+1):
    total += pow(-1, i+1) * i
print(int(total))
