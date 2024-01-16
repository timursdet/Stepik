m, n = int(input()), int(input())
if m < n:
    i = m
    for i in range(m, n + 1):
        print(i)
if n <= m:
    i = n
    for i in range(m, n-1, -1):
        print(i)