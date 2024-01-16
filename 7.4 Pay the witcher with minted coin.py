total = int(0)
money = int(input())
while money >= 25:
    total = total + money//25
    money = money%25
while money >= 10:
    total = total + money//10
    money = money%10
while money >= 5:
    total = total + money//5
    money = money%5
while money >= 1:
    total = total + money//1
    money = money%1
print(total)