print("Лодка, река 2 рыбака")
print("Максимальная масса, которую выдерживает лодка")
m = int(input())
print("Количество рыбаков, которое нужно перевести")
n1 = int(input())

if n1 % 2 > 0:
    n=n1+1
else:
    n=n1
print("Введите вес каждого из ", (n1), "рыбаков")
res = []

for i in range(n1):
    a = int(input())
    res.append(a)
res.sort()

max_ves = max(res)
min_ves = min(res)
cost = 0
if max_ves > m:
    print("задача не имеет решения т.к. вес некоторых пассажиров тяжелее грузоподьемности лодки")
elif (max_ves + min_ves) <= m:
    x = int(n/2)
else:
    while (max(res)+min(res)) >= m:
        res.pop()
        cost +=1
    x = int(n1 - cost)/2
    if (n1 - cost) % 2 > 0:
        print("Для переправы необходимо минимум ",int(x+cost+1)," лодок")
    else:
        print("Для переправы необходимо минимум ",int(x+cost)," лодок")