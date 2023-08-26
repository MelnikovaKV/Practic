print("Запускается проект! Кто из инвесторов сможет участвовать?")

print("Какая минимальная сумма нужна для участия?")
proekt = int(input())
print("Какая сумма есть у Майка?")
mike = int(input())
print("Какая сумма есть у Ивана?")
ivan = int(input())

print("Кто из инвесторов сможет вложиться в СтартАп?")
if mike >= proekt and ivan >= proekt:
    print("Mike и Ivan")
    print(2)
else:
    if mike >= proekt and ivan < proekt:
        print("Mike")
    else:
        if mike < proekt and ivan >= proekt:
            print("Ivan")
        else:
            if mike + ivan >= proekt:
                print("Смогут вместе")
                print(1)
            else:
                print("В этом проекте они участвовать не смогут")
                print(0)