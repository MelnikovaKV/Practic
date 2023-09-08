print("Какие евсть четные числа между этими?")
print("Введите число А :")
a = int(input())
print("Введите число B (большее, чем число А):")
b = int(input())
print("Все четные числа от ", (a), " до ", (b), " : ")
c = a % 2
d = a-1
e = a-2
if c < 1:
    while e <= (b-2):
        e += 2
        print(e, end=' ')
else:
    while d <= (b-2):
        d += 2
        print(d, end=' ')