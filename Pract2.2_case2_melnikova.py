print("Введите любое целое число из пяти знаков")
a = int(input())
b = int(a % 10)
c = int(a // 10 % 10)
d = int(a // 100 % 10)
e = int(a // 1000 % 10)
f = int(a // 10000 % 10)
print("ответ на задание")
print(float((c**b)*d/(f-e)))