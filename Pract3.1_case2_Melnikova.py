print("Сколько натуральных делителей у числа?")
print("Введите число :")
x = int(input())
cost = 0
for i in range(1, x+1):
    if x % i == 0:
        cost += 1
    else:
        cost += 0
print("у числа", (x),"существует", (cost), "натуральных делителей")