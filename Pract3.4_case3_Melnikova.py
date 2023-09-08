print("Введите значения  элементов через пробел")
res = list(map(int, input().split()))
mnzh = set()
print("Элемент повторяется? YES / NO")
for i in range(len(res)):
    if res[i] in mnzh:
        print((res[i]),'YES')
    else:
        print((res[i]),'NO')
        mnzh.add(res[i])
