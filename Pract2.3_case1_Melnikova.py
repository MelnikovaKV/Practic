print("Я отгадаю вид числа с одной попытки! Проверим?")
print("Введите любое целое число")
a = (int(input()))
b = a % 2
if a < 0 and b < 1:
    print("Отрицательное чётное число")
elif (a < 0) and b > 0:
    print("Отрицательное нечётное число")
elif (a > 0) and (b < 1):
    print("Положительное чётное число")
elif a > 0 and b > 0:
    print("Положительное число, не является чётным")
else:
    print("Вы ввели НОЛЬ")
print("Cыграем еще?")