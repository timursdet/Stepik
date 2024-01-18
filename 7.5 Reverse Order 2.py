num = int(input())
new_num = str("")
while num != 0:
    last_digit = num % 10
    new_num = new_num + str(last_digit)
    num = num // 10
print(new_num)
print(new_num)
