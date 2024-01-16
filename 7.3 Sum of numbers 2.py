counter = 0
n = int(input())
for i in range(1, n+1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        counter += i
print(counter)