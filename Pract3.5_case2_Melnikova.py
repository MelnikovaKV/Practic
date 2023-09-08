# Создать словарь : ключ = число, значение = число в своей-же степени, шаг = 1
bank = {}
a = int(input("первое значение ключа: "))
b = int(input("последнее значение ключа: "))
keys = list(range(a, b+1))
values = []

for i in range(len(keys)):
    a = int(keys[i])**int(keys[i])
    values.append(a)
bank = dict(zip(keys, values))
for key,value in bank.items():
    print(key, ':', value)