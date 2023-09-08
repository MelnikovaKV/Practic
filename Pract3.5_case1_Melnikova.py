name = input("Кличка питомца: ")
vid = input("Вид питомца: ")
age = int(input("Возраст питомца: "))
owner = input("Имя владельца: ")
pets = {name:{"Вид питомца: ": vid, "Возраст питомца: " : int(age),"Имя владельца: " : owner}}

if int(age) >= 5 and int(age) <=20:
    cost = str("лет")
elif age % 10 == 1:
    cost = str("год")
elif age % 10 == 2:
    cost = str("года")
elif age % 10 == 3:
    cost = str("года")
elif age % 10 == 4:
    cost = str("года")
else:
    cost = str("лет")
print("Это ",(vid)," по кличке ",(name),". Возраст питомца: ",int(age),(str(cost)),". Имя владельца: ",(owner),".")