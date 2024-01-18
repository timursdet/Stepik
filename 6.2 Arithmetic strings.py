# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
#
# Формат входных данных
# На вход программе подаются три строки, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

a ,b , c = input(), input(), input()
a_len = int(len(a))
b_len = int(len(b))
c_len = int(len(c))
max_len = int(max(a_len, b_len, c_len))
min_len = int(min(a_len, b_len, c_len))
avg_len = int((a_len + b_len + c_len) - min_len - max_len)
if max_len - avg_len == avg_len - min_len:
    print("YES")
else:
    print('NO')