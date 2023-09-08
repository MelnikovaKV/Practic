print("введите кол-во элементов первого списка")
n1 = int(input())
print("Введите значения ",(n1)," элементов первого списка")
spisok1 = []
for i in range(n1):
    el = input()
    spisok1.append(el)

print("введите кол-во элементов второго списка")
n2 = int(input())
print("Введите значения ",(n2)," элементов второго списка")
spisok2 = []
for i in range(n2):
    el = input()
    spisok2.append(el)

print(list(spisok1))
print(list(spisok2))
print("В этих списках пересекаются ", len(list(set(spisok1)&set(spisok2))), "элемента, со значениями : ",list(set(spisok1)&set(spisok2)))