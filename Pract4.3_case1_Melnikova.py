'''Напишите рекурсивную функцию,которая выведет все элементы от первого до последнего
и в конце отобразит сообщение Конец списка, если выводить больше нечего.
Циклы использовать запрещено'''

my_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def el(my_list):
    if my_list == []:
        print("Конец списка.")
    else:
        print(my_list.pop(0))
        el(my_list)

el(my_list)