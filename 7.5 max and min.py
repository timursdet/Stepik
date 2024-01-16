num = int(input())
max_num = int(0)
min_num = int(10)
while num != 0:
    last_digit = num % 10
    max_num = max(max_num, last_digit)
    min_num = min(min_num, last_digit)
    num = num // 10
print('Максимальная цифра равна', max_num)
print('Минимальная цифра равна', min_num)