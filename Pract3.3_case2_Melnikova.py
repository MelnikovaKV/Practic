print("Задайте количество элементов")
n = int(input())
print("задайте данные этих ", (n), "элементов, через пробел")
res = list(map(int, input().split()))
print("Ваш список выглядит так:")
print(*res)

print("этот же список, только начиная с крайнего элемента:")