"""Задание №1
● Создайте функцию, которая принимает в качестве параметра -
натуральное целое число.
● Данная функция находит факториал полученного числа
Например, факториал числа 3 это число 6.
● Теперь создайте список факториалов чисел от получившегося ранее
факториала 6, до 1.
В итоге, на вход программа получает например число 3, возвращает число 6
(факториал числа 3) и вам нужно сделать список из факториалов числа 6 в
убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 -
это 120 и так далее вплоть до 1
То есть, результирующий список будет выглядеть в нашем примере так:
[720, 120, 24, 6, 2, 1]"""


'''n = int(input('Введите число, для которого нужно вычислить факториал: '))
f = 1
a = 1
res1 = []
for i in range(n):
    f = f * a
    a = a + 1
    print (a)
    

c = 1
b = 1
res = []
for i in range(f):
    c = c * b
    b = b + 1
    res.append(c)
res.reverse()
print(res)'''


def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
y=int(input('Введите число, для которого нужно вычислить факториал: '))
m = fac(y)
print(m)
res = []
for i in range(m,0,-1):
    res.append(fac(i))
print('Факториал числа ', y, 'равен:', m)
print('Факториалы чисел, предшествующих ', m, 'равны:')
print(res)