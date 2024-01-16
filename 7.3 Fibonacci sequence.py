n1 = 1
n2 = 0
n = int(input())
for i in range(n):
    n2, n1 = n1, n1+n2
    print(n2, sep='', end=' ')