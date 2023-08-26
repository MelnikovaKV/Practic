print("Сколько гласных букв в твоем слове?")
print("Напиши слово латиницей, в котором есть буквы a e i a o")
slovo = (input())

count = 0
glasnye = set("aeiou")
for letter in slovo:
    if letter in glasnye:
        count += 1
a = 0
bukvaa = set("a")
for letter in slovo:
    if letter in bukvaa:
        a += 1
e = 0
bukvae = set("e")
for letter in slovo:
    if letter in bukvae:
        e += 1
u = 0
bukvau = set("u")
for letter in slovo:
    if letter in bukvau:
        u += 1
i = 0
bukvai = set("i")
for letter in slovo:
    if letter in bukvai:
        i += 1
o = 0
bukvao = set("o")
for letter in slovo:
    if letter in bukvao:
        o += 1

if a<1 or e<1 or u<1 or i<1 or o<1:
    print("Количество гласных равно:")
    print(count)
    print("Но в твоем слове есть не все нужные гласные")
    print("Посчитаю каждую, если в слове будут все нужные буквы")
    print ("False")
else:
    print("Количество гласных равно:")
    print(count)
    print("А именно : ")
    print("a = ",(a),"; e = ",(e),"; i = ",(i),"; o = ",(o),"; u = ",(u))