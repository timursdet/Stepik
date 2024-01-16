largest1 = -1
largest2 = -1
n = int(input())
for i in range(n):
    number = int(input())
    if number > largest1:
        largest2 = largest1
        largest1 = number
    elif number > largest2:
        largest2 = number
print(largest1, largest2, sep='\n')

