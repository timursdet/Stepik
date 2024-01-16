flag = True
for i in range(10):
    n = int(input())
    if n % 2 == 1:
        flag = False
if flag:
    print('YES')
else:
    print('NO')

