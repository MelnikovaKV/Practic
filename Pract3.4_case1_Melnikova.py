print("Задайте количество элементов")
n = int(input())
print("задайте данные этих ", (n), "элементов, через пробел")
res = list(map(int, input().split()))
mnzh = set(res)

povtor_mnzh = set()
povtor_elements = set()

for i in res:
    if i in povtor_mnzh:
        povtor_elements.add(i)
    else:
        povtor_mnzh.add(i)

print("В списке ", len(povtor_elements), " повторяющихся элементов")
