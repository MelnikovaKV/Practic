print("Задайте количество элементов")
n = int(input())
print("задайте данные этих ", (n), "элементов")
res = []
for i in range(n):
    a = int(input())
    res.append(a)
print("Ваш список выглядит так:")
print(*res)
print("этот же список, только в обратную сторону:")
res.reverse()
print(*res)